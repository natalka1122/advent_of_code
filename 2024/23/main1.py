from __future__ import annotations
import re

# FILENAME = "demo.txt"  # expected 7
FILENAME = "input.txt"
T = "t"


def f(node: str, the_map: dict[str, set[str]]) -> set[tuple[str, str, str]]:
    result = set()
    for node1 in the_map[node]:
        for node2 in the_map[node1]:
            if node in the_map[node2]:
                result.add(tuple(sorted([node, node1, node2])))
    return result


def main() -> None:
    the_map: dict[str, set[str]] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"^(\w\w)-(\w\w)$", line.strip())
            if line_match is None:
                raise NotImplementedError
            a, b = line_match.groups()
            if a not in the_map:
                the_map[a] = set()
            if b not in the_map:
                the_map[b] = set()
            the_map[a].add(b)
            the_map[b].add(a)
    print(the_map)
    triplets: set[tuple[str, str, str]] = set()
    for node in filter(lambda x: x.startswith(T), the_map):
        triplets.update(f(node, the_map))
    print(len(triplets))


if __name__ == "__main__":
    main()
