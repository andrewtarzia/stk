"""
Terminal Alkene Factory
=======================

"""

from __future__ import annotations

import typing
from collections import abc

from . import functional_group_factory as _functional_group_factory
from . import utilities as _utilities
from .. import functional_groups as _functional_groups
from ... import molecule as _molecule
from ...atoms import elements as _elements

__all__ = (
    'TerminalAlkeneFactory',
)

_ValidIndex = typing.Literal[0, 1, 2, 3, 4, 5]


class TerminalAlkeneFactory(
    _functional_group_factory.FunctionalGroupFactory,
):
    # This docstring is a literal string, to silence a flake8 warning
    # about CH\ :sub:`2`. It's taking the backslash out of context.
    r"""
    Creates :class:`.Alkene` instances.

    Creates functional groups from substructures, which match the
    ``[*][C]([*])=[C]([H])[H]`` functional group string.

    Examples:

        *Creating Functional Groups with the Factory*

        You want to create a building block which has
        :class:`.Alkene` functional groups, but only if they are
        terminal. You want the non-terminal carbon atom in those
        functional groups to be the *bonder* atom, and the terminal
        CH\ :sub:`2` group to be the *deleter* atoms.

        .. testcode:: creating-functional-groups-with-the-factory

            import stk

            building_block = stk.BuildingBlock(
                smiles='C=CCCCCC=C',
                functional_groups=(stk.TerminalAlkeneFactory(), ),
            )

        .. testcode:: creating-functional-groups-with-the-factory
            :hide:

            assert all(
                isinstance(functional_group, stk.Alkene)
                for functional_group
                in building_block.get_functional_groups()
            )
            assert building_block.get_num_functional_groups() == 2

        *Changing the Bonder and Deleter Atoms*

        You want to create a building block which has
        :class:`.Alkene` functional groups, but only if they are
        terminal. You want the carbon atoms to be the *bonder* atoms
        and you don't want any *deleter* atoms.

        .. testcode:: changing-the-bonder-and-deleter-atoms

            import stk

            terminal_alkene_factory = stk.TerminalAlkeneFactory(
                # The indices of the carbon atoms in the functional
                # group string (see docstring) are 1 and 3.
                bonders=(1, 3),
                deleters=(),
            )
            building_block = stk.BuildingBlock(
                smiles='C=CCCCCC=C',
                functional_groups=(terminal_alkene_factory, ),
            )

        .. testcode:: changing-the-bonder-and-deleter-atoms
            :hide:

            fg1, fg2 = building_block.get_functional_groups()
            assert fg1.get_num_bonders() == 2
            assert sum(1 for _ in fg1.get_deleters()) == 0
            assert fg2.get_num_bonders() == 2
            assert sum(1 for _ in fg2.get_deleters()) == 0

            assert all(
                isinstance(atom, stk.C)
                for functional_group
                in building_block.get_functional_groups()
                for atom
                in functional_group.get_bonders()
            )

    See Also:

        :class:`.GenericFunctionalGroup`
            Defines *bonders* and  *deleters*.

    """

    def __init__(
        self,
        bonders: tuple[_ValidIndex, ...] = (1, ),
        deleters: tuple[_ValidIndex, ...] = (3, 4, 5),
        placers: typing.Optional[tuple[_ValidIndex, ...]] = None,
    ) -> None:
        """
        Initialize a :class:`.TerminalAlkeneFactory` instance.

        Parameters:

            bonders:
                The indices of atoms in the functional group string,
                which are *bonder* atoms.

            deleters:
                The indices of atoms in the functional group string,
                which are *deleter* atoms.

            placers:
                The indices of atoms in the functional group string,
                which are *placer* atoms. If ``None``, `bonders` will
                be used.

        """

        self._bonders = bonders
        self._deleters = deleters
        self._placers = bonders if placers is None else placers

    def get_functional_groups(
        self,
        molecule: _molecule.Molecule,
    ) -> abc.Iterable[_functional_groups.Alkene]:

        for atom_ids in _utilities.get_atom_ids(
            query='[*][C]([*])=[C]([H])[H]',
            molecule=molecule,
        ):
            atoms = tuple(molecule.get_atoms(atom_ids))
            yield _functional_groups.Alkene(
                carbon1=typing.cast(_elements.C, atoms[1]),
                atom1=atoms[0],
                atom2=atoms[2],
                carbon2=typing.cast(_elements.C, atoms[3]),
                atom3=atoms[4],
                atom4=atoms[5],
                bonders=tuple(atoms[i] for i in self._bonders),
                deleters=tuple(atoms[i] for i in self._deleters),
                placers=tuple(atoms[i] for i in self._placers),
            )
