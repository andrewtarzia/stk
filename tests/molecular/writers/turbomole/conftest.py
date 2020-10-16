import pytest
import stk

from .case_data import CaseData

bb1 = stk.BuildingBlock('BrCCBr', [stk.BromoFactory()])
bb2 = stk.BuildingBlock('BrCC(CBr)CBr', [stk.BromoFactory()])
topology_graph = stk.cof.PeriodicHoneycomb(
    building_blocks=(bb1, bb2),
    lattice_size=(1, 1, 1),
)
cof = stk.ConstructedMolecule(topology_graph)


@pytest.fixture(
    params=(
        CaseData(
            molecule=bb1,
            writer=stk.TurbomoleWriter(),
            string=(
                '$coord angs\n -1.4238 1.5615 0.3223 Br\n -0.7405 -0.2'
                '573 0.128 C\n 0.7148 -0.1157 -0.3383 C\n 1.6267 0.889'
                '6 1.0687 Br\n -1.3518 -0.8075 -0.5939 H\n -0.7769 -0.'
                '6964 1.144 H\n 0.7695 0.528 -1.2387 H\n 1.1821 -1.102'
                '2 -0.4922 H\n$end\n'
            ),
            periodic_info=None,
        ),
        CaseData(
            molecule=cof,
            writer=stk.TurbomoleWriter(),
            string=(
                '$periodic 3\n$cell angs\n   36.432   36.431  105.166 '
                ' 90.00  90.00  60.00\n$coord angs\n 19.4675 11.2392 5'
                '2.5831 C\n 18.2205 10.5214 53.0065 C\n 16.9674 11.238'
                '9 52.5831 C\n 18.2126 9.0717 52.5831 C\n 20.3559 10.6'
                '937 52.9602 H\n 19.4494 12.2444 53.05 H\n 18.2209 10.'
                '5188 54.1253 H\n 16.8933 12.1964 53.1311 H\n 16.1039 '
                '10.6163 52.92 H\n 18.198 8.9414 51.4898 H\n 17.295 8.'
                '586 52.9733 H\n 35.18 20.3106 52.5831 C\n 36.427 21.0'
                '285 53.0065 C\n 37.6801 20.3109 52.5831 C\n 36.4349 2'
                '2.4781 52.5831 C\n 34.2916 20.8561 52.9602 H\n 35.198'
                '1 19.3054 53.05 H\n 36.4266 21.031 54.1253 H\n 37.754'
                '2 19.3534 53.1311 H\n 38.5436 20.9335 52.92 H\n 36.44'
                '95 22.6084 51.4898 H\n 37.3525 22.9638 52.9733 H\n 26'
                '.6592 16.1586 52.5831 C\n 27.9883 15.3912 52.5831 C\n'
                ' 26.5169 16.7343 53.5027 H\n 26.5749 16.78 51.6703 H'
                '\n 27.9769 14.6019 53.3609 H\n 28.845 16.0773 52.6866'
                ' H\n 18.2158 -0.7674 52.5831 C\n 18.2158 0.7674 52.58'
                '31 C\n 17.4593 -1.1784 53.2584 H\n 18.1216 -1.1511 51'
                '.5485 H\n 18.541 1.1522 53.5702 H\n 17.2359 1.1662 52'
                '.2734 H\n 9.7725 16.1586 52.5831 C\n 8.4433 15.3912 5'
                '2.5831 C\n 9.9306 16.7069 53.5167 H\n 10.6097 15.4759'
                ' 52.3392 H\n 7.5905 16.0988 52.593 H\n 8.4022 14.6647'
                ' 53.4111 H\n$end\n'
            ),
            periodic_info=topology_graph.get_periodic_info(),
        ),
    ),
)
def case_data(request):

    return request.param
