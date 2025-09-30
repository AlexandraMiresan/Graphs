class Vertex:
    def __init__(self, vertex_id:int):
        self.__id = vertex_id
        self.__inbound_edges = []
        self.__outbound_edges = []

    @property
    def id(self):
        return self.__id

    @property
    def inbound_edges(self):
        return self.__inbound_edges

    @property
    def outbound_edges(self):
        return self.__outbound_edges

    def add_inbound_edge(self, edge):
        self.__inbound_edges.append(edge)

    def add_outbound_edge(self, edge):
        self.__outbound_edges.append(edge)

    def get_in_degree(self):
        return len(self.inbound_edges)

    def get_out_degree(self):
        return len(self.outbound_edges)


