import copy
from itertools import permutations
from operator import truediv

from Edge import Edge
from Vertex import Vertex


class DirectedGraph:
    def __init__(self):
        self.__number_of_vertices = 0
        self.__number_of_edges = 0
        self.__vertices = {}
        self.__edges = {}

    @property
    def vertices(self):
        return self.__vertices

    @property
    def edges(self):
        return self.__edges

    @property
    def number_of_vertices(self):
        return self.__number_of_vertices

    @property
    def number_of_edges(self):
        return self.__number_of_edges


    def parse_vertices(self):
        for vertex in self.__vertices:
            yield vertex

    def check_edge(self, start_vertex:Vertex, end_vertex:Vertex):
        for edge in start_vertex.outbound_edges:
            if edge.end_vertex == end_vertex:
                return edge.id

        return -1

    def parse_outbound_edges(self, start_vertex:Vertex):
        for edge in start_vertex.outbound_edges:
            yield edge.id

    def parse_inbound_edges(self, end_vertex:Vertex):
        for edge in end_vertex.inbound_edges:
            yield edge.id

    def get_in_degree(self, vertex:Vertex):
        return vertex.get_in_degree()

    def get_out_degree(self, vertex:Vertex):
        return vertex.get_out_degree()

    def get_endpoints_by_edge_id(self, edge_id:Edge.id):
        if edge_id in self.__edges.keys():
            return self.__edges[edge_id].start_vertex.id, self.__edges[edge_id].end_vertex.id
        else:
            return -1, -1

    def add_edge(self, start_vertex:Vertex, end_vertex:Vertex, cost:int):
        if start_vertex.id + Edge.ID_SEPARATOR + end_vertex.id in self.__edges.keys():
            raise ValueError("The edge already exists!")
        edge = Edge(start_vertex, end_vertex, cost)
        self.__edges[edge.id] = edge
        self.__number_of_edges = len(self.__edges)

        start_vertex.outbound_edges.append(edge)
        end_vertex.inbound_edges.append(edge)

    def add_vertex(self, vertex_id):
        if vertex_id in self.__vertices.keys():
            raise ValueError("The vertex already exists!")
        vertex = Vertex(vertex_id)
        self.__vertices[vertex.id] = vertex
        self.__number_of_vertices = len(self.__vertices)

    def remove_edge(self, edge_id):
        if edge_id not in self.__edges.keys():
            raise ValueError("The edge does not exist!")

        edge_to_remove = self.__edges[edge_id]
        edge_to_remove.start_vertex.outbound_edges.remove(edge_to_remove)
        edge_to_remove.end_vertex.inbound_edges.remove(edge_to_remove)

        self.__edges.pop(edge_id)
        self.__number_of_edges = len(self.__edges)

    def remove_vertex(self, vertex_id):
        if vertex_id not in self.__vertices.keys():
            raise ValueError("The vertex does not exist!")

        vertex_to_remove = self.__vertices[vertex_id]
        for edge in vertex_to_remove.outbound_edges:
            self.remove_edge(edge.id)

        self.__vertices.pop(vertex_id)
        self.__number_of_vertices = len(self.__vertices)

    def update_cost(self, edge_id:Edge.id, newcost:int):
        exists = False
        for edge in self.__edges.keys():
            if edge_id == edge:
                self.__edges[edge_id].cost = newcost
                exists = True

        if not exists:
            raise ValueError("The edge does not exist!")

    def copy(self):
        return copy.deepcopy(self)

    def bfs(self, start: Vertex):
        queue = [start]
        dist = {start: 0}
        parent = {start: None}

        while queue:
            vertex = queue.pop(0)
            for edge in vertex.outbound_edges:
                neighbor = edge.end_vertex
                if neighbor not in dist:
                    dist[neighbor] = dist[vertex] + 1
                    parent[neighbor] = vertex
                    queue.append(neighbor)

        return dist, parent

    def shortest_path(self, start:Vertex, end:Vertex):
        _,parent = self.bfs(start)
        return self.retrieve_path(parent,end)

    def retrieve_path(self, parent, end):
        if end not in parent.keys():
            return None
        vertex = end
        path = []
        while vertex is not None:
            path.append(vertex)
            vertex = parent[vertex]
        path.reverse()
        return path

#problem 7

    def floyd_warshall(self):
        dist = {}
        next_vertex = {}

        # Initialize distances
        for v in self.__vertices.values():
            dist[v.id] = {}
            next_vertex[v.id] = {}
            for u in self.__vertices.values():
                if v == u:
                    dist[v.id][u.id] = 0
                else:
                    dist[v.id][u.id] = float('inf')
                next_vertex[v.id][u.id] = None

        # Initialize distances from edges
        for edge in self.__edges.values():
            u = edge.start_vertex.id
            v = edge.end_vertex.id
            dist[u][v] = edge.cost
            next_vertex[u][v] = v

        # Floyd-Warshall core loop
        for k in self.__vertices:
            for i in self.__vertices:
                for j in self.__vertices:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_vertex[i][j] = next_vertex[i][k]

        return dist, next_vertex

    def reconstruct_path(self, start_id, end_id, next_vertex):
        if next_vertex[start_id][end_id] is None:
            return None  # No path exists

        path = [start_id]
        while start_id != end_id:
            start_id = next_vertex[start_id][end_id]
            path.append(start_id)

        return path

    def lowest_cost_walk(self, start_id, end_id):
        dist, next_vertex = self.floyd_warshall()
        path = self.reconstruct_path(start_id, end_id, next_vertex)
        if path is None:
            return float('inf'), None
        return dist[start_id][end_id], path


    def tsp_setup(self):
        dist, _ = self.floyd_warshall()

        vertex_ids = sorted(self.__vertices.keys())
        nr_of_vertices = self.__number_of_vertices


        cost_matrix = [[float('inf')] * nr_of_vertices for _ in range(nr_of_vertices)]

        for i in range(nr_of_vertices):
            for j in range(nr_of_vertices):
                from_id = vertex_ids[i]
                to_id = vertex_ids[j]
                cost_matrix[i][j] = dist[from_id][to_id]

        return cost_matrix, vertex_ids




    def tsp(self):
        minCost = float('inf')
        cost_matrix, vertex_ids = self.tsp_setup()
        nr_of_vertices = self.__number_of_vertices
        id_to_index = {vertex_ids[i]: i for i in range(nr_of_vertices)}

        path = []

        for perm in permutations(vertex_ids):
            currCost = 0
            valid = True

            for i in range(nr_of_vertices - 1):
                from_index = id_to_index[perm[i]]
                to_index = id_to_index[perm[i + 1]]

                if cost_matrix[from_index][to_index] == float('inf'):
                    valid = False
                    break
                currCost += cost_matrix[from_index][to_index]

            if valid:
                from_index = id_to_index[perm[-1]]
                to_index = id_to_index[perm[0]]

                if cost_matrix[from_index][to_index] != float('inf'):
                    currCost += cost_matrix[from_index][to_index]

                if currCost < minCost:
                    minCost = currCost
                    path= list(perm) + [perm[0]]

            if not path:
                return float('inf'), []


        return minCost, path


    def totalCost(self, cost_matrix, visited, currPos, nr_of_vertices, count, costSoFar, ans, currPath, bestPath):
        if count == nr_of_vertices and cost_matrix[currPos][0] != 0:
            total_cost = min(ans[0], costSoFar + cost_matrix[currPos][0])
            if total_cost < ans[0]:
                ans[0] = total_cost
                bestPath.clear()
                bestPath.extend(currPath + [0])
            return

        for i in range(nr_of_vertices):
            if not visited[i] and cost_matrix[currPos][i] != 0:
                visited[i] = True
                currPath.append(i)
                self.totalCost(cost_matrix, visited, i, nr_of_vertices, count + 1, costSoFar + cost_matrix[currPos][i], ans, currPath, bestPath)
                visited[i] = False
                currPath.pop()

    def tsp_bakctracking(self):
        cost_matrix, vertex_ids = self.tsp_setup()
        nr_of_vertices = self.__number_of_vertices

        visited = [False] * nr_of_vertices
        visited[0] = True

        ans = [float('inf')]
        currPath = [0]
        bestPath = []

        self.totalCost(cost_matrix, visited, 0, nr_of_vertices, 1, 0, ans, currPath, bestPath)

        resPath = [vertex_ids[i] for i in bestPath]
        return ans[0], resPath













