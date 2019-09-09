# Stubs for networkx.drawing.nx_pydot (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

basestring = str
unicode = str

def write_dot(G: Any, path: Any) -> None: ...
def read_dot(path: Any): ...
def from_pydot(P: Any): ...
def to_pydot(N: Any): ...
def graphviz_layout(G: Any, prog: str = ..., root: Optional[Any] = ...): ...
def pydot_layout(G: Any, prog: str = ..., root: Optional[Any] = ...): ...