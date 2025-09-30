from DirectedGraph import DirectedGraph


class ReadWrite:
    @staticmethod
    def read_from_file(file_name):
        directed_graph = DirectedGraph()
        fin = open(file_name, "rt")
        number_of_vertices, number_of_edges = fin.readline().split(" ")
        number_of_edges = number_of_edges.strip()

        for edge in range(int(number_of_edges)):
            start_vertex_id, end_vertex_id, cost = fin.readline().split(" ")
            cost = cost.strip()
            if start_vertex_id not in directed_graph.vertices.keys():
                directed_graph.add_vertex(start_vertex_id)
            if end_vertex_id not in directed_graph.vertices.keys():
                directed_graph.add_vertex(end_vertex_id)
            directed_graph.add_edge(directed_graph.vertices[start_vertex_id], directed_graph.vertices[end_vertex_id],
                                    int(cost))

        fin.close()
        return directed_graph

    @staticmethod
    def write_to_file(directed_graph: DirectedGraph, file_name):
        fout = open(file_name, "wt")
        fout.write(str(directed_graph.number_of_vertices) + " " + str(directed_graph.number_of_edges) + "\n")

        for edge in directed_graph.edges.values():
            fout.write(str(edge.start_vertex.id) + " " + str(edge.end_vertex.id) + " " + str(edge.cost) + "\n")

        fout.close()
