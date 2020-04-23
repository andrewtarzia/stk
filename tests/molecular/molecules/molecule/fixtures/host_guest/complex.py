import pytest
import stk

from ...case_data import CaseData


_cage = stk.ConstructedMolecule(
    topology_graph=stk.cage.FourPlusSix(
        building_blocks={
            stk.BuildingBlock(
                smiles='BrC1=C(Br)[C+]=[C+]1',
                functional_groups=[stk.BromoFactory()],
            ): (4, 5, 6, 7, 8),
            stk.BuildingBlock(
                smiles='BrC1=C(Br)[C+]=N1',
                functional_groups=[stk.BromoFactory()],
            ): (9, ),
            stk.BuildingBlock(
                smiles=(
                    'Br[C+]1[C+2][C+](Br)[C+]2[C+][C+2]C2('
                    'Br)[C+2]1'
                ),
                functional_groups=[stk.BromoFactory()],
            ): (0, 1, 2),
            stk.BuildingBlock(
                smiles=(
                    'Br[C+]1[C+2][C+](Br)[C+]2[C+](F)[C+2]'
                    'C2(Br)[C+2]1'
                ),
                functional_groups=[stk.BromoFactory()],
            ): (3, ),
        },
    ),
)


@pytest.fixture(
    params=(
        CaseData(
            molecule=stk.ConstructedMolecule(
                topology_graph=stk.host_guest.Complex(
                    host=stk.BuildingBlock.init_from_molecule(_cage),
                    guest=stk.BuildingBlock('C#N'),
                )
            ),
            smiles=(
                'F[C+]1[C+2]C23[C+2][C+]4[C+2][C+](C5=C(N=[C+]5)[C+]5'
                '[C+2][C+]6[C+2]C7([C+2][CH+][C+]57)C5=C([C+]=[C+]5)['
                'C+]5[C+2][C+]([C+2]C7([C+2][CH+][C+]57)C5=C2[C+]=[C+'
                ']5)C2=C([C+]=[C+]2)[C+]2[C+2][C+](C5=C4[C+]=[C+]5)[C'
                '+]4[CH+][C+2]C4([C+2]2)C2=C6[C+]=[C+]2)[C+]13.[H]C#N'
            ),
        ),
    ),
)
def host_guest_complex(request):
    return request.param
