from UndirectedGraph import UndirectedGraph


class UI:
    def __init__(self, graph:UndirectedGraph):
        self.__graph = graph

    def print_menu(self):
        print("1. Prim's Algorithm.")
        print("0. Exit.")

    def start_UI(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    self.prims_algorithm()
                case "0":
                    break
                case default:
                    print("Invalid choice!")

    def prims_algorithm(self):
        mst_edges = self.__graph.prims_algorithm()
        for edge in mst_edges:
            print(f"{edge.start_vertex.id} -- {edge.end_vertex.id} : {edge.cost}")
