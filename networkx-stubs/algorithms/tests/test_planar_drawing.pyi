# Stubs for networkx.algorithms.tests.test_planar_drawing (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def test_graph1() -> None: ...
def test_graph2() -> None: ...
def test_circle_graph() -> None: ...
def test_grid_graph() -> None: ...
def test_one_node_graph() -> None: ...
def test_two_node_graph() -> None: ...
def test_three_node_graph() -> None: ...
def test_multiple_component_graph1() -> None: ...
def test_multiple_component_graph2() -> None: ...
def test_invalid_half_edge() -> None: ...
def test_triangulate_embedding1() -> None: ...
def test_triangulate_embedding2() -> None: ...
def check_triangulation(embedding: Any, expected_embedding: Any) -> None: ...
def check_embedding_data(embedding_data: Any) -> None: ...
def is_close(a: Any, b: Any, rel_tol: float = ..., abs_tol: float = ...): ...
def point_in_between(a: Any, b: Any, p: Any): ...
def check_edge_intersections(G: Any, pos: Any) -> None: ...

class Vector:
    x: Any = ...
    y: Any = ...
    node: Any = ...
    quadrant: int = ...
    def __init__(self, x: Any, y: Any, node: Any) -> None: ...
    def __eq__(self, other: Any): ...
    def __lt__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __ge__(self, other: Any): ...

def planar_drawing_conforms_to_embedding(embedding: Any, pos: Any): ...