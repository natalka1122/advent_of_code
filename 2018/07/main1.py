FILENAME = "demo.txt"  # expected CABDFE
FILENAME = "input.txt"


class Node:
    def __init__(self) -> None:
        self.reqire: set[str] = set()

    def add_req(self, exclude: str) -> None:
        self.reqire.add(exclude)


def main() -> None:
    nodes: dict[str, Node] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            n1 = line.split(" ")[1]
            n2 = line.split(" ")[7]
            if n1 not in nodes:
                nodes[n1] = Node()
            if n2 not in nodes:
                nodes[n2] = Node()
            nodes[n2].add_req(n1)
    executed: set[str] = set()
    while len(nodes) > 0:
        for node_name in sorted(nodes):
            if all(map(lambda x: x in executed, nodes[node_name].reqire)):
                print(node_name, end="")
                executed.add(node_name)
                del nodes[node_name]
                break
    print()


if __name__ == "__main__":
    main()
