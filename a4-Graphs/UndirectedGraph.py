import heapq

from Edge import Edge
from Vertex import Vertex


class UndirectedGraph:
    def __init__(self):
        self.__number_of_vertices = 0
        self.__number_of_edges = 0
        self.__vertices = {}
        self.__edges = {}

    @property
    def number_of_vertices(self):
        return self.__number_of_vertices

    @property
    def number_of_edges(self):
        return self.__number_of_edges

    @property
    def vertices(self):
        return self.__vertices

    @property
    def edges(self):
        return self.__edges

    def add_vertex(self, vertex_id):
        if vertex_id in self.__vertices.keys():
            raise ValueError("Vertex already added.")
        vertex = Vertex(vertex_id)
        self.__vertices[vertex_id] = vertex
        self.__number_of_vertices = len(self.__vertices)

    def add_edge(self, start_vertex:Vertex, end_vertex:Vertex, cost:int):
        if (start_vertex.id + Edge.ID_SEPARATOR + end_vertex.id in self.__edges.keys()) or (end_vertex.id + Edge.ID_SEPARATOR + start_vertex.id in self.__edges.keys()):
            raise ValueError("Edge already added.")
        edge = Edge(start_vertex, end_vertex, cost)
        self.__edges[edge.id] = edge
        self.__number_of_edges = len(self.__edges)

        start_vertex.edges.append(edge)
        end_vertex.edges.append(edge)

    def is_connected(self):
        if not self.__vertices:
            return True

        visited = set()
        start_vertex = next(iter(self.__vertices.values()))

        def dfs(vertex:Vertex):
            visited.add(vertex.id)
            for edge in vertex.edges:
                neighbor = edge.get_other_vertex(vertex)
                if neighbor.id not in visited:
                    dfs(neighbor)

        dfs(start_vertex)
        return len(visited) == self.__number_of_vertices


    def prims_algorithm(self):
        visited = set()
        min_heap = []
        mst =[]

        start_vertex = next(iter(self.__vertices.values()))
        visited.add(start_vertex.id)

        for edge in start_vertex.edges:
            neighbor = edge.get_other_vertex(start_vertex)
            heapq.heappush(min_heap, (edge.cost, start_vertex.id, neighbor.id,edge))

        while min_heap and len(visited) < self.__number_of_vertices:
            cost, from_id, to_id, edge = heapq.heappop(min_heap)

            if to_id in visited:
                continue

            mst.append(edge)
            visited.add(to_id)

            to_vertex = self.__vertices[to_id]

            for neighbor_edge in to_vertex.edges:
                neighbor_vertex = neighbor_edge.get_other_vertex(to_vertex)
                if neighbor_vertex.id not in visited:
                    heapq.heappush(min_heap, (neighbor_edge.cost, to_id, neighbor_vertex.id, neighbor_edge))

        return mst

#problem6