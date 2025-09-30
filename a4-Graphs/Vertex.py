class Vertex:
    def __init__(self, vertex_id:int):
        self.__id = vertex_id
        self.__edges = []

    @property
    def id(self):
        return self.__id

    @property
    def edges(self):
        return self.__edges