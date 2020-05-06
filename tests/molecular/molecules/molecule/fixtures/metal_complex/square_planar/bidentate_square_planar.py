import pytest
import stk
from rdkit.Chem import AllChem as rdkit

from ....case_data import CaseData


atom = rdkit.MolFromSmiles('[Pd+2]')
atom.AddConformer(rdkit.Conformer(atom.GetNumAtoms()))

_palladium_atom = stk.BuildingBlock.init_from_rdkit_mol(atom)
atom_0, = _palladium_atom.get_atoms(0)
_palladium_atom = _palladium_atom.with_functional_groups(
    (stk.SingleAtom(atom_0) for i in range(4))
)

_bi_1 = stk.BuildingBlock.init_from_file(
    smiles='NCCN',
    functional_groups=[
        stk.SmartsFunctionalGroupFactory(
            smarts='[#7]~[#6]',
            bonders=(0, ),
            deleters=(),
        ),
    ]
)


@pytest.fixture(
    params=(
        CaseData(
            molecule=stk.ConstructedMolecule(
                stk.metal_complex.BiDentateSquarePlanar(
                    metals={_palladium_atom: 0},
                    ligands={_bi_1: (0, 1)},
                    reaction_factory=stk.DativeReactionFactory(
                        stk.GenericReactionFactory(
                            bond_orders={
                                frozenset({
                                    stk.GenericFunctionalGroup,
                                    stk.SingleAtom
                                }): 9
                            }
                        )
                    )
                )
            ),
            smiles=('C1CN->[Pd+2]2(<-N1)<-NCCN->2'),
        ),
    ),
)
def metal_complex_bidentatesquareplanar(request):
    return request.param
