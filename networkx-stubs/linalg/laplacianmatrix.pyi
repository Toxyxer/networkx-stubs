# Stubs for networkx.linalg.laplacianmatrix (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def laplacian_matrix(G: Any, nodelist: Optional[Any] = ..., weight: str = ...): ...
def normalized_laplacian_matrix(G: Any, nodelist: Optional[Any] = ..., weight: str = ...): ...
def directed_laplacian_matrix(G: Any, nodelist: Optional[Any] = ..., weight: str = ..., walk_type: Optional[Any] = ..., alpha: float = ...): ...
def directed_combinatorial_laplacian_matrix(G: Any, nodelist: Optional[Any] = ..., weight: str = ..., walk_type: Optional[Any] = ..., alpha: float = ...): ...