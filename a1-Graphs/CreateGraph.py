from random import random, randint

from DirectedGraph import DirectedGraph


class CreateGraph:

    @staticmethod
    def createGraph(number_of_vertices: int, number_of_edges: int):
        directed_graph = DirectedGraph()

        for key in range(number_of_vertices):
            directed_graph.add_vertex(str(key))

        while directed_graph.number_of_edges < number_of_edges:
            try:
                start_vertex = str(randint(0, number_of_vertices - 1))
                end_vertex = str(randint(0, number_of_vertices - 1))
                cost = randint(0, 100)
                directed_graph.add_edge(directed_graph.vertices[start_vertex], directed_graph.vertices[end_vertex],
                                        cost)
            except ValueError:
                continue
        return directed_graph
