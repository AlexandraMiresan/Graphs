from Vertex import Vertex


class Edge:
    ID_SEPARATOR = "#"
    def __init__(self, start, end, cost):
        self.__start_vertex = start
        self.__end_vertex = end
        self.__cost = cost
        global ID_SEPARATOR
        self.__id = start.id + self.ID_SEPARATOR + end.id

    @property
    def start_vertex(self):
        return self.__start_vertex

    @property
    def end_vertex(self):
        return self.__end_vertex

    @property
    def id(self):
        return self.__id

    @property
    def cost(self):
        return self.__cost

    def get_other_vertex(self, vertex:Vertex):
        if vertex == self.__start_vertex:
            return self.__end_vertex
        elif vertex == self.__end_vertex:
            return self.__start_vertex
        else:
            raise ValueError("Vertex not part of this edge.")