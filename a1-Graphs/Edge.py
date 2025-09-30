from Vertex import Vertex


class Edge:
    ID_SEPARATOR = '#'

    def __init__(self, start_vertex: Vertex, end_vertex: Vertex, cost: int):
        self.__start_vertex = start_vertex
        self.__end_vertex = end_vertex
        self.__cost = cost
        global ID_SEPARATOR
        self.__id = start_vertex.id + self.ID_SEPARATOR + end_vertex.id

    @property
    def start_vertex(self):
        return self.__start_vertex

    @property
    def end_vertex(self):
        return self.__end_vertex

    @property
    def cost(self):
        return self.__cost

    @property
    def id(self):
        return self.__id

    @cost.setter
    def cost(self, cost):
        self.__cost = cost
