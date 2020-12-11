"""
Two Plus Four
=============

"""

from ..cage import Cage
from ..vertices import _LinearCageVertex, _NonLinearCageVertex
from ...topology_graph import Edge


class TwoPlusFour(Cage):
    """
    Represents a capsule cage topology graph.

    Nonlinear building blocks with four functional groups are
    required for this topology.

    Linear building blocks with two functional groups are required for
    this topology.

    When using a :class:`dict` for the `building_blocks` parameter,
    as in :ref:`multi-building-block-cage-construction`:
    *Multi-Building Block Cage Construction*, a :class:`.BuildingBlock`
    needs to be assigned to each of the following vertex ids:

        | 4-functional group: (0, 1)
        | 2-functional group: (2, 3, 4, 5)

    See :class:`.Cage` for more details and examples.

    """

    _vertex_prototypes = (
        _NonLinearCageVertex(0, [0, 0, -1]),
        _NonLinearCageVertex(1, [0, 0, 1]),

        _LinearCageVertex(2, [2, 0, 0], False),
        _LinearCageVertex(3, [-2, 0, 0], False),
        _LinearCageVertex(4, [0, 2, 0], False),
        _LinearCageVertex(5, [0, -2, 0], False),
    )

    _edge_prototypes = (
        Edge(0, _vertex_prototypes[2], _vertex_prototypes[0]),
        Edge(1, _vertex_prototypes[2], _vertex_prototypes[1]),
        Edge(2, _vertex_prototypes[3], _vertex_prototypes[0]),
        Edge(3, _vertex_prototypes[3], _vertex_prototypes[1]),
        Edge(4, _vertex_prototypes[4], _vertex_prototypes[0]),
        Edge(5, _vertex_prototypes[4], _vertex_prototypes[1]),
        Edge(6, _vertex_prototypes[5], _vertex_prototypes[0]),
        Edge(7, _vertex_prototypes[5], _vertex_prototypes[1])
    )

    _num_windows = 4
    _num_window_types = 1
