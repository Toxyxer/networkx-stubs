# Stubs for networkx.readwrite.graphml (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def write_graphml_xml(G: Any, path: Any, encoding: str = ..., prettyprint: bool = ..., infer_numeric_types: bool = ...) -> None: ...
def write_graphml_lxml(G: Any, path: Any, encoding: str = ..., prettyprint: bool = ..., infer_numeric_types: bool = ...) -> None: ...
def generate_graphml(G: Any, encoding: str = ..., prettyprint: bool = ...) -> None: ...
def read_graphml(path: Any, node_type: Any = ..., edge_key_type: Any = ...): ...
def parse_graphml(graphml_string: Any, node_type: Any = ...): ...

class GraphML:
    NS_GRAPHML: str = ...
    NS_XSI: str = ...
    NS_Y: str = ...
    SCHEMALOCATION: Any = ...
    unicode: Any = ...
    long: Any = ...
    types: Any = ...
    xml_type: Any = ...
    python_type: Any = ...
    convert_bool: Any = ...

class GraphMLWriter(GraphML):
    myElement: Any = ...
    infer_numeric_types: Any = ...
    prettyprint: Any = ...
    encoding: Any = ...
    xml: Any = ...
    keys: Any = ...
    attributes: Any = ...
    attribute_types: Any = ...
    def __init__(self, graph: Optional[Any] = ..., encoding: str = ..., prettyprint: bool = ..., infer_numeric_types: bool = ...) -> None: ...
    def attr_type(self, name: Any, scope: Any, value: Any): ...
    def get_key(self, name: Any, attr_type: Any, scope: Any, default: Any): ...
    def add_data(self, name: Any, element_type: Any, value: Any, scope: str = ..., default: Optional[Any] = ...): ...
    def add_attributes(self, scope: Any, xml_obj: Any, data: Any, default: Any) -> None: ...
    def add_nodes(self, G: Any, graph_element: Any) -> None: ...
    def add_edges(self, G: Any, graph_element: Any) -> None: ...
    def add_graph_element(self, G: Any) -> None: ...
    def add_graphs(self, graph_list: Any) -> None: ...
    def dump(self, stream: Any) -> None: ...
    def indent(self, elem: Any, level: int = ...) -> None: ...

class IncrementalElement:
    xml: Any = ...
    prettyprint: Any = ...
    def __init__(self, xml: Any, prettyprint: Any) -> None: ...
    def append(self, element: Any) -> None: ...

class GraphMLWriterLxml(GraphMLWriter):
    myElement: Any = ...
    infer_numeric_types: Any = ...
    xml: Any = ...
    keys: Any = ...
    attribute_types: Any = ...
    def __init__(self, path: Any, graph: Optional[Any] = ..., encoding: str = ..., prettyprint: bool = ..., infer_numeric_types: bool = ...) -> None: ...
    def add_graph_element(self, G: Any) -> None: ...
    def add_attributes(self, scope: Any, xml_obj: Any, data: Any, default: Any) -> None: ...
    def dump(self) -> None: ...
write_graphml = write_graphml_xml
write_graphml = write_graphml_lxml

class GraphMLReader(GraphML):
    node_type: Any = ...
    edge_key_type: Any = ...
    multigraph: bool = ...
    edge_ids: Any = ...
    def __init__(self, node_type: Any = ..., edge_key_type: Any = ...) -> None: ...
    xml: Any = ...
    def __call__(self, path: Optional[Any] = ..., string: Optional[Any] = ...) -> None: ...
    def make_graph(self, graph_xml: Any, graphml_keys: Any, defaults: Any, G: Optional[Any] = ...): ...
    def add_node(self, G: Any, node_xml: Any, graphml_keys: Any, defaults: Any) -> None: ...
    def add_edge(self, G: Any, edge_element: Any, graphml_keys: Any) -> None: ...
    def decode_data_elements(self, graphml_keys: Any, obj_xml: Any): ...
    def find_graphml_keys(self, graph_element: Any): ...