# Stubs for networkx.algorithms.operators.binary (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, TypeVar, Union

from networkx.classes.graph import Graph


def union(G: Any, H: Any, rename: Any = ..., name: Optional[Any] = ...): ...
def disjoint_union(G: Any, H: Any): ...
def intersection(G: Any, H: Any): ...
def difference(G: Any, H: Any): ...
def symmetric_difference(G: Any, H: Any): ...



X = TypeVar('X', covariant=True)
Y = TypeVar('Y', covariant=True)
GT = TypeVar('GT', bound=Graph)
#TODO: This does not handle the cases when graphs of different types are passed which is allowed
def compose(G: GT[X], H: GT[Y]) -> GT[Union[X,Y]]: ...
