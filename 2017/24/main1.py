from __future__ import annotations
from collections.abc import Iterator

FILENAME = "demo.txt"  # expected 31
FILENAME = "input.txt"
ZERO = 0


def calc_path(path: list[tuple[int, int]]) -> int:
    return sum(map(lambda x: x[0] + x[1], path))


def get_path(
    start_bridge: tuple[int, int],
    bridges: set[tuple[int, int]],
    path: list[tuple[int, int]] | None = None,
) -> Iterator[int]:
    if path is None:
        path = []
    sorted_start_bridge = tuple(sorted(start_bridge))
    if len(sorted_start_bridge) != 2:
        raise NotImplementedError
    path = path + [sorted_start_bridge]
    yield calc_path(path)
    filtered_bridges = filter(lambda x: x not in path and start_bridge[1] in x, bridges)
    for bridge in filtered_bridges:
        if bridge[0] == start_bridge[1]:
            yield from get_path(bridge, bridges, path)
        elif bridge[1] == start_bridge[1]:
            yield from get_path(bridge[::-1], bridges, path)
        else:
            raise NotImplementedError


def main() -> None:
    bridges: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            bridge = sorted(map(int, line.split("/")))
            if len(bridge) != 2:
                raise NotImplementedError
            bridges.add((bridge[0], bridge[1]))
    print(bridges)
    best_path = 0
    for start_bridge in filter(lambda x: x[0] == ZERO, bridges):
        for path in get_path(start_bridge, bridges):
            best_path = max(best_path, path)
    print(best_path)


if __name__ == "__main__":
    main()
