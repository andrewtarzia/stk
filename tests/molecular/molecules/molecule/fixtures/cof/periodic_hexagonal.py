import pytest
import stk

from ...case_data import CaseData


@pytest.fixture(
    params=(
        CaseData(
            molecule=stk.ConstructedMolecule(
                topology_graph=stk.cof.PeriodicHexagonal(
                    building_blocks={
                        stk.BuildingBlock(
                            smiles='BrC1=C(Br)[C+]=N1',
                            functional_groups=[stk.BromoFactory()],
                        ): (
                            4, 5, 6, 7, 8, 9, 20, 21, 23, 24, 30, 36,
                            38, 40, 41, 42, 43, 46, 47, 52, 53, 60, 61,
                        ),
                        stk.BuildingBlock(
                            smiles='BrN1N(Br)[C+]=N1',
                            functional_groups=[stk.BromoFactory()],
                        ): (
                            10, 11, 12, 13, 14, 15, 22, 25, 26, 27, 28,
                            29, 37, 39, 44, 45, 54, 55, 56, 57, 58, 59,
                            31, 62, 63,
                        ),
                        stk.BuildingBlock(
                            smiles=(
                                'Br[C+]1[C+]2[N+][C+2]C2(Br)[C+](I)[C+'
                                '](I)[C+](Br)[C+]1Br'
                            ),
                            functional_groups=[
                                stk.BromoFactory(),
                                stk.IodoFactory(),
                                stk.FluoroFactory(),
                            ],
                        ): (0, 1, 18, 50, 51),
                        stk.BuildingBlock(
                            smiles=(
                                'Br[C+]1[C+]2[S][C+2]C2(Br)[C+](I)[C+]'
                                '(I)[C+](Br)[C+]1Br'
                            ),
                            functional_groups=[
                                stk.BromoFactory(),
                                stk.IodoFactory(),
                                stk.FluoroFactory(),
                            ],
                        ): (2, 16, 34, 49),
                        stk.BuildingBlock(
                            smiles=(
                                'Br[C+]1[C+]2[S][O]C2(Br)[C+](I)[C+](I'
                                ')[C+](Br)[C+]1Br'
                            ),
                            functional_groups=[
                                stk.BromoFactory(),
                                stk.IodoFactory(),
                                stk.FluoroFactory(),
                            ],
                        ): (3, 17, 19, 32, 33, 35, 48),
                    },
                    lattice_size=(2, 2, 1),
                    vertex_alignments={0: 5},
                ),
            ),
            smiles=(
                '[C+]1=NC2=C1[C+]1[C+]3[C+]4[C+]5C6=C(N=[C+]6)[C+]6[C+'
                ']7[C+]8C9=C(N=[C+]9)[C+]9[C+]%10[C+]%11[C+]%12[C+]%13'
                'C%14=C(N=[C+]%14)[C+]%14[C+]%15C%16=C(N=[C+]%16)[C+]%'
                '16[C+]%17[C+]%18[C+]%19C%20=C(N=[C+]%20)[C+]%20[C+]%2'
                '1C%22=C([C+]=N%22)[C+]%22[C+]([C+]%23[NH2+][C+2]C%23('
                '[C+]%23[C+]%24C%25=C(N=[C+]%25)[C+]%25[C+]%26C%27=C(['
                'C+]=N%27)[C+]%27[C+](C%28=C([C+]=N%28)[C+]%28[C+]%29['
                'C+]%30C%31=C(N=[C+]%31)C%31%32OS[C+]%31[C+]%31C%33=C('
                'N=[C+]%33)[C+]([C+]%33[C+]%25N%25[C+]=NN%25[C+]%25[C+'
                ']%34C%35=C(N=[C+]%35)C%35%36[C+2][NH2+][C+]%35[C+]%35'
                'C%37=C(N=[C+]%37)[C+]%37[C+]%38[C+](C%39=C(N=[C+]%39)'
                'C9%39[C+2][NH2+][C+]%13%39)[C+]9[C+]%13[C+]%39SOC%39%'
                '37C%37=C([C+]=N%37)[C+]%34[C+]%34C%37=C(N=[C+]%37)C%3'
                '7%39OS[C+]%37[C+]%37C%40=C([C+]=N%40)[C+]([C+]%21N%21'
                'N=[C+]N%21[C+]%34[C+]%21S[C+2]C%21%25N%21N=[C+]N%21[C'
                '+]%22%24)[C+]%21SOC%21%22[C+]%20C%20=C([C+]=N%20)[C+]'
                '%20[C+](C%21=C(N=[C+]%21)C%21(OS[C+]5%21)[C+]1N1N=[C+'
                ']N1%22)[C+]1C5=C(N=[C+]5)C65[C+2][NH2+][C+]5[C+](C5=C'
                '([C+]=N5)[C+]%35[C+]5C6=C([C+]=N6)[C+]1[C+]1S[C+2]C1('
                '[C+]%20N1N=[C+]N%181)N1N=[C+]N1[C+]([C+]([C+]%32N1N=['
                'C+]N1C1(OS[C+]%151)[C+]1[C+]([C+]%14N6N=[C+]N96)N6N=['
                'C+]N6[C+]([C+]([C+]2%37)N2[C+]=NN2[C+]([C+]%30N2[C+]='
                'NN12)C1([C+2][NH2+][C+]%281)N1N=[C+]N31)[C+]%39N1N=[C'
                '+]N%131)N1[C+]=NN%171)[C+]%31N1[C+]=NN1[C+]5[C+]%36N1'
                'N=[C+]N%331)[C+]8N1N=[C+]N%381)C1(OS[C+]%261)N1N=[C+]'
                'N%291)[C+]([C+]([C+](N1N=[C+]N%101)C1([C+2]S[C+]%271)'
                'N1[C+]=NN%231)N1N=[C+]N71)N1N=[C+]N41)N1[C+]=NN%111)N'
                '1[C+]=NN1[C+]%19C1([C+2]S[C+]%161)N1N=[C+]N%121'
            ),
        ),
    ),
)
def cof_periodic_hexagonal(request):
    return request.param
