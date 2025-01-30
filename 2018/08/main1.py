from __future__ import annotations

FILENAME = "demo.txt"  # expected 138
FILENAME = "input.txt"

NONE_INT = -100500


class Node:
    def __init__(
        self, index: int, parent: Node | None = None, parent_index: int | None = None
    ) -> None:
        self.name = chr(ord("A") + index)
        self.parent = parent
        self.parent_index = parent_index
        self.children: list[Node] = []
        self.metadata: list[int] = []
        self.children_left: int = NONE_INT
        self.medatata_left: int = NONE_INT

    def __repr__(self) -> str:
        return f"Node({self.name})"


def main() -> None:
    current_node = Node(0)
    nodes: list[Node] = [current_node]
    is_child_count = True
    is_medatata_count = False
    is_medatata = False
    with open(FILENAME, "r") as file:
        for line in file:
            for number in map(int, line.split(" ")):
                # print(number, nodes)
                if is_child_count:
                    if current_node.children_left != NONE_INT:
                        raise NotImplementedError
                    current_node.children_left = number
                    is_child_count = False
                    is_medatata_count = True
                elif is_medatata_count:
                    if current_node.medatata_left != NONE_INT:
                        raise NotImplementedError
                    current_node.medatata_left = number
                    is_medatata_count = False
                    if current_node.children_left > 0:
                        current_node.children_left -= 1
                        next_node = Node(
                            len(nodes), parent=current_node, parent_index=len(current_node.children)
                        )
                        current_node.children.append(next_node)
                        nodes.append(next_node)
                        current_node = next_node
                        is_child_count = True
                    elif current_node.medatata_left > 0:
                        is_medatata = True
                    else:
                        # Not possible because there are one or more metadata entries
                        raise NotImplementedError
                elif is_medatata:
                    if current_node.medatata_left <= 0:
                        raise NotImplementedError
                    current_node.metadata.append(number)
                    current_node.medatata_left -= 1
                    if current_node.medatata_left == 0:
                        if current_node.parent is None:
                            break
                        current_node = current_node.parent
                        if current_node.children_left == 0:
                            pass
                        else:
                            is_medatata = False
                            current_node.children_left -= 1
                            next_node = Node(
                                len(nodes),
                                parent=current_node,
                                parent_index=len(current_node.children),
                            )
                            current_node.children.append(next_node)
                            nodes.append(next_node)
                            current_node = next_node
                            is_child_count = True
                else:
                    raise NotImplementedError

    # print(nodes)
    print(sum(map(lambda x: sum(x.metadata), nodes)))


if __name__ == "__main__":
    main()
