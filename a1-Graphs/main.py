from ReadWrite import ReadWrite
from UI import UI


def main():
    graph = ReadWrite.read_from_file("random_graph1.txt")
    ui = UI(graph)
    ui.start_UI()
    # copy_graph = graph.copy()
    # ReadWrite.write_to_file(copy_graph, "copy_graph.txt")
    # copy_graph.remove_edge("6#2")
    # ReadWrite.write_to_file(graph, "initial_graph.txt")
    # ReadWrite.write_to_file(copy_graph, "copy_graph2.txt")

#problem6


if __name__ == "__main__":
    main()