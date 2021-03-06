# Stubs for networkx.algorithms.tests.test_euler (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from unittest import TestCase

class TestIsEulerian(TestCase):
    def test_is_eulerian(self) -> None: ...
    def test_is_eulerian2(self) -> None: ...

class TestEulerianCircuit(TestCase):
    def test_eulerian_circuit_cycle(self) -> None: ...
    def test_eulerian_circuit_digraph(self) -> None: ...
    def test_multigraph(self) -> None: ...
    def test_multigraph_with_keys(self) -> None: ...
    def test_not_eulerian(self) -> None: ...

class TestEulerize(TestCase):
    def test_disconnected(self) -> None: ...
    def test_null_graph(self) -> None: ...
    def test_null_multigraph(self) -> None: ...
    def test_on_empty_graph(self) -> None: ...
    def test_on_eulerian(self) -> None: ...
    def test_on_eulerian_multigraph(self) -> None: ...
    def test_on_complete_graph(self) -> None: ...
