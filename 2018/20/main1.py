from __future__ import annotations
from collections.abc import Iterator
from queue import SimpleQueue

FILENAME = "demo1_1.txt"  # expected 3
FILENAME = "demo1_2.txt"  # expected 10
FILENAME = "demo1_3.txt"  # expected 18
FILENAME = "demo1_4.txt"  # expected 23
FILENAME = "demo1_5.txt"  # expected 31
FILENAME = "input.txt"

DIRECTION = {"W": (0, -1), "E": (0, 1), "N": (-1, 0), "S": (1, 0)}
OPEN_BRACKET = "("
CLOSE_BRACKET = ")"
OR_SYMBOL = "|"

Point = tuple[int, int]


class Links:
    def __init__(self) -> None:
        self.l: set[tuple[Point, Point]] = set()

    def __repr__(self) -> str:
        return str(self.l)

    def add(self, n1: Point, n2: Point) -> None:
        if n1 < n2:
            self.l.add((n1, n2))
        elif n1 > n2:
            self.l.add((n2, n1))
        else:
            raise NotImplementedError

    def append(self, other: Links) -> None:
        self.l.update(other.l)

    def get_nei(self, node: Point) -> Iterator[Point]:
        for n1, n2 in self.l:
            if n1 == node:
                yield n2
            elif n2 == node:
                yield n1


def get_links(line: str, start: Point) -> Links:
    result = Links()
    node = start
    index = 0
    while index < len(line):
        if line[index] == OPEN_BRACKET:
            stack = 0
            index += 1
            inside_brackets = ""
            while stack > 0 or line[index] != CLOSE_BRACKET:
                if line[index] == OPEN_BRACKET:
                    stack += 1
                elif line[index] == CLOSE_BRACKET:
                    stack -= 1
                inside_brackets += line[index]
                index += 1
            # print(inside_brackets)
            result.append(get_links(inside_brackets, node))
        elif line[index] == CLOSE_BRACKET:
            raise NotImplementedError
        elif line[index] == OR_SYMBOL:
            node = start
        elif line[index] in DIRECTION:
            dy, dx = DIRECTION[line[index]]
            new_node = node[0] + dy, node[1] + dx
            result.add(node, new_node)
            node = new_node
        else:
            raise NotImplementedError
        index += 1

    return result


def f(line: str) -> int:
    start_node = (0, 0)
    links = get_links(line, start_node)
    visited: set[Point] = {start_node}
    Q: SimpleQueue[tuple[Point, int]] = SimpleQueue()
    Q.put_nowait((start_node, 0))
    while not Q.empty():
        node, path = Q.get_nowait()
        for nei in links.get_nei(node):
            # print(f"nei = {nei}")
            if nei in visited:
                continue
            Q.put_nowait((nei, path + 1))
            visited.add(nei)
    print(node, path)
    return path


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()[1:-1]))


if __name__ == "__main__":
    main()
