

from CreateGraph import CreateGraph
from DirectedGraph import DirectedGraph
from Edge import Edge
from ReadWrite import ReadWrite
from Vertex import Vertex


class UI:
    def __init__(self, graph:DirectedGraph):
        self.__graph = graph

    def print_menu(self):
        print("1. Get the number of vertices.")
        print("2. Get the number of edges.")
        print("3. Iterate the set of vertices.")
        print("4. Check if there is an edge from a vertex to another.")
        print("5. Get the in degree and the out degree of a specific vertex.")
        print("6. Iterate the set of outbound edges of a specific vertex.")
        print("7. Iterate the set of inbound edges of a specific vertex.")
        print("8. Get the endpoints of an edge.")
        print("9. Update cost of an edge.")
        print("10. Add vertex.")
        print("11. Remove vertex.")
        print("12. Add edge.")
        print("13. Remove edge.")
        print("14. Generate random graph.")
        print("15. Find the lowest length path between two vertices.")
        print("16. Find the lowest cost path between two vertices.")
        print("17. TSP with permutations.")
        print("18. TSP with backtracking.")
        print("0. Exit.")
        print()

    def start_UI(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.get_number_of_vertices()
                case "2":
                    self.get_number_of_edges()
                case "3":
                    self.iterate_vertices()
                case "4":
                    self.check_edge()
                case "5":
                    self.get_in_out_degree()
                case "6":
                    self.iterate_outbound_edges()
                case "7":
                    self.iterate_inbound_edges()
                case "8":
                    self.get_endpoints()
                case "9":
                    self.update_cost()
                case "10":
                    self.add_vertex()
                case "11":
                    self.remove_vertex()
                case "12":
                    self.add_edge()
                case "13":
                    self.remove_edge()
                case "14":
                    self.generate_graph()
                case "15":
                    self.lowest_length_path()
                case "16":
                    self.lowest_cost_path_ui()
                case "17":
                    self.tsp()
                case "18":
                    self.tsp_backtracking()
                case "0":
                    break

    def tsp_backtracking(self):
        minCost, path = self.__graph.tsp_bakctracking()
        print("Min cost: " + str(minCost))
        print("Path: " + str(path))
        print()

    def tsp(self):
        minCost, path = self.__graph.tsp()
        print("Min cost: " + str(minCost))
        print("Path: " + str(path))
        print()

    def get_number_of_vertices(self):
        print(self.__graph.number_of_vertices)

    def iterate_vertices(self):
        for vertice in self.__graph.parse_vertices():
            print(vertice)

    def check_edge(self):
        try:
            start_vertex = input("Enter start vertex: ")
            end_vertex = input("Enter end vertex: ")

            if start_vertex in self.__graph.vertices.keys() and end_vertex in self.__graph.vertices.keys():
                if self.__graph.check_edge(self.__graph.vertices[start_vertex], self.__graph.vertices[end_vertex]) == -1:
                    print("The edge does not exist.")
                    print()
                else:
                    print(self.__graph.check_edge(self.__graph.vertices[start_vertex], self.__graph.vertices[end_vertex]))
                    print()

        except ValueError as e:
            print(e)

    def get_in_out_degree(self):
        try:
            vertex_id = input("Enter vertex number: ")
            exists = False
            for vertex in self.__graph.vertices.keys():
                if vertex == vertex_id:
                    exists = True
                    print("The in degree of the vertex is: " + str(self.__graph.vertices[vertex].get_in_degree()))
                    print("The out degree of the vertex is: " + str(self.__graph.vertices[vertex].get_out_degree()))
                    print()

            if not exists:
                print("The vertex does not exist.")
        except ValueError as e:
            print(e)

    def iterate_outbound_edges(self):
        try:
            vertex_id =input("Enter vertex number: ")
            exists = False
            for vertex in self.__graph.vertices.keys():
                if vertex == vertex_id:
                    for vertice in self.__graph.parse_outbound_edges(self.__graph.vertices[vertex_id]):
                        print(vertice)
                    exists = True

            if not exists:
                print("The vertex does not exist.")
        except ValueError as e:
            print(e)

    def iterate_inbound_edges(self):
        try:
            vertex_id = input("Enter vertex number: ")
            exists = False
            for vertex in self.__graph.vertices.keys():
                if vertex == vertex_id:
                    for vertice in self.__graph.parse_inbound_edges(self.__graph.vertices[vertex_id]):
                        print(vertice)
                    exists = True

            if not exists:
                print("The vertex does not exist.")
        except ValueError as e:
            print(e)

    def get_endpoints(self):
        try:
            edge_id = input("Enter edge_id: ")
            if self.__graph.get_endpoints_by_edge_id(edge_id) == (-1, -1):
                print("The edge does not exist.")
                print()
            else:
                print(self.__graph.get_endpoints_by_edge_id(edge_id))
                print()
        except ValueError as e:
            print(e)

    def update_cost(self):
        try:
            start_vertex = input("Enter start vertex: ")
            end_vertex = input("Enter end vertex: ")
            cost = input("Enter cost of an edge: ")
            self.__graph.update_cost(start_vertex + Edge.ID_SEPARATOR + end_vertex, int(cost))
            ReadWrite.write_to_file(self.__graph,"test.txt")
        except ValueError as e:
            print(e)

    def add_vertex(self):
        try:
            vertex_id = int(input("Enter vertex number: "))
            self.__graph.add_vertex(Vertex(vertex_id))
            print("The vertex has been added.")
        except ValueError as e:
            print(e)

    def remove_vertex(self):
        try:
            vertex_id = input("Enter vertex number: ")
            self.__graph.remove_vertex(vertex_id)
            print("The vertex has been removed.")
        except ValueError as e:
            print(e)

    def remove_edge(self):
        try:
            start_vertex = input("Enter start vertex: ")
            end_vertex = input("Enter end vertex: ")
            self.__graph.remove_edge(start_vertex + Edge.ID_SEPARATOR + end_vertex)
            print("The edge has been removed.")
        except ValueError as e:
            print(e)

    def add_edge(self):
        try:
            start_vertex = input("Enter start vertex: ")
            end_vertex = input("Enter end vertex: ")
            cost = int(input("Enter cost of an edge: "))
            self.__graph.add_edge(self.__graph.vertices[start_vertex], self.__graph.vertices[end_vertex], cost)
            print("The edge has been added.")
            print()
        except ValueError as e:
            print(e)
            print()

    def check_if_graph_is_valid(self, number_of_vertices, number_of_edges):
        if number_of_vertices * (number_of_vertices - 1) < number_of_edges:
            raise ValueError("The graph you want to create is invalid!")


    def generate_graph(self):
        try:
            number_of_vertices = int(input("Enter number of vertices: "))
            number_of_edges = int(input("Enter number of edges: "))
            self.check_if_graph_is_valid(number_of_vertices, number_of_edges)
            new_graph = CreateGraph.createGraph(number_of_vertices, number_of_edges)
            file_name = input("Enter file name: ")
            print()
            ReadWrite.write_to_file(new_graph, file_name)
        except ValueError as e:
            print(e)
            print()

    def get_number_of_edges(self):
        print(self.__graph.number_of_edges)

    def print_graph(self, graph):
        ReadWrite.write_to_file(graph, "test.txt")

    def lowest_length_path(self):
        start = input("Enter start vertex id: ")
        end = input("Enter end vertex id: ")
        print()

        if start not in self.__graph.vertices or end not in self.__graph.vertices:
            print("One or both of the vertices do not exist.")
            print()
            return

        start_vertex = self.__graph.vertices[start]
        end_vertex = self.__graph.vertices[end]

        path = self.__graph.shortest_path(start_vertex, end_vertex)
        if path is None:
            print("No path exists between the given vertices.")
            print()
        else:
            print("Shortest path:", " -> ".join(v.id for v in path))
            print()

    def lowest_cost_path_ui(self):
        start = input("Enter start vertex id: ")
        end = input("Enter end vertex id: ")
        print()

        if start not in self.__graph.vertices or end not in self.__graph.vertices:
            print("One or both of the vertices do not exist.")
            print()
            return

        try:
            cost, path = self.__graph.lowest_cost_walk(start, end)
            if path is None:
                print("No walk exists between the given vertices.")
            else:
                print("Lowest cost walk:", " -> ".join(path))
                print("Total cost:", cost)
            print()
        except Exception as e:
            print(f"An error occurred: {e}")








