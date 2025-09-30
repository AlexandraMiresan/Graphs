from ReadWrite import ReadWrite
from UI import UI


def main():
    try:
        graph = ReadWrite.read_from_file("graph.txt")
        ui = UI(graph)
        ui.start_UI()
    except ValueError as err:
        print(err)


if __name__ == "__main__":
    main()
