import pytest
import stk

from ..case_data import CaseData

topology_graph = stk.polymer.Linear(
    building_blocks=(
        stk.BuildingBlock('BrCCBr', [stk.BromoFactory()]),
    ),
    repeating_unit='A',
    num_repeating_units=2,
)


@pytest.fixture(
    params=(
        CaseData(
            fitness_normalizer=stk.Sum(
                filter=lambda population, record:
                    record.get_fitness_value() is not None,
            ),
            population=(
                stk.MoleculeRecord(
                    topology_graph=topology_graph,
                ).with_fitness_value((1, -5, 5)),
                stk.MoleculeRecord(
                    topology_graph=topology_graph,
                ).with_fitness_value((3, -10, 2)),
                stk.MoleculeRecord(
                    topology_graph=topology_graph,
                ).with_fitness_value((2, 20, 1)),
                stk.MoleculeRecord(topology_graph),
            ),
            normalized=(
                stk.MoleculeRecord(
                    topology_graph=topology_graph,
                ).with_fitness_value(1),
                stk.MoleculeRecord(
                    topology_graph=topology_graph,
                ).with_fitness_value(-5),
                stk.MoleculeRecord(
                    topology_graph=topology_graph,
                ).with_fitness_value(23),
                stk.MoleculeRecord(topology_graph),
            ),
        ),
    ),
)
def sum(request):
    return request.param
