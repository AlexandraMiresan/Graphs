from UndirectedGraph import UndirectedGraph


class ReadWrite:
    @staticmethod
    def read_from_file(filename):
        undirected_graph = UndirectedGraph()
        fin = open(filename, "rt")
        number_of_vertices, number_of_edges = fin.readline().split(" ")
        number_of_edges = number_of_edges.strip()

        for edge in range(int(number_of_edges)):
            start_vertex_id, end_vertex_id, cost = fin.readline().split(" ")
            cost = cost.strip()
            if start_vertex_id not in undirected_graph.vertices.keys():
                undirected_graph.add_vertex(start_vertex_id)
            if end_vertex_id not in undirected_graph.vertices.keys():
                undirected_graph.add_vertex(end_vertex_id)
            undirected_graph.add_edge(undirected_graph.vertices[start_vertex_id], undirected_graph.vertices[end_vertex_id], int(cost))


        fin.close()
        if undirected_graph.is_connected():
            return undirected_graph
        else:
            raise ValueError("Graph is not connected")

    @staticmethod
    def write_to_file(undirected_graph: UndirectedGraph, filename):
        fout = open(filename, "wt")
        fout.write(str(undirected_graph.number_of_vertices) + " " + str(undirected_graph.number_of_edges) + "\n")

        for edge in undirected_graph.edges.values():
            fout.write(str(edge.start_vertex_id) + " " + str(edge.end_vertex_id) + " " + str(edge.cost) + "\n")

        fout.close()