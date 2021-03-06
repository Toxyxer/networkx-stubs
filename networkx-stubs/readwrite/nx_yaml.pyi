# Stubs for networkx.readwrite.nx_yaml (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from io import TextIOWrapper
from typing import Any, NewType
from networkx import Graph

Path = str | TextIOWrapper


def write_yaml(
    G_to_be_yaml: Graph[Any],
    path_for_yaml_output: Path,
    **kwds: Any) -> None: ...


def read_yaml(path: Path) -> Graph[Any]: ...
