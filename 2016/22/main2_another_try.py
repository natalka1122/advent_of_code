from __future__ import annotations
from typing import Any
import re

FILENAME = "demo.txt"  # expected 7
FILENAME = "input.txt"

DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
MAX_Y = 6
SMALL_VS_BIG = 100


# class Node:
#     def __init__(
#         self,
#         coord: tuple[int, int],
#         has_data: bool,
#         used: int,
#         avail: int,
#     ):
#         self.name: str = f"disk {coord}"
#         self.has_data: bool = has_data
#         self.used: int = used
#         self.avail: int = avail
#         self.nei: None | set[Node] = None

#     def define_nei(self, neis: set[Node]) -> None:
#         if self.nei is not None:
#             raise NotImplementedError
#         self.nei = neis

#     def __eq__(self, other: Any) -> bool:
#         if not isinstance(other, Node):
#             return False
#         return (
#             self.name == other.name
#             and self.has_data == other.has_data
#             and self.used == other.used
#             and self.avail == other.avail
#         )

#     def __hash__(self) -> int:
#         return hash((self.name, self.has_data, self.used, self.avail))

#     def __repr__(self) -> str:
#         return f"{self.name}: ({self.used}, {self.avail})" + (
#             " DATA" if self.has_data else ""
#         )

#     def __lt__(self, other: Any) -> bool:
#         if not isinstance(other, Node):
#             return False
#         return self.name < other.name


class Disks(tuple[tuple[int, int]]):
    def __new__(cls, data: tuple[tuple[int, int]], *_: object) -> Disks:
        return super(Disks, cls).__new__(cls, tuple(data))

    def __init__(
        self,
        _: object,
        source_index: int,
        target_index: int,
        neis: dict[int, set[int]],
    ):
        self.source_index = source_index
        self.target_index = target_index
        self.neis = neis

    @property
    def is_ready(self) -> bool:
        return self.source_index == self.target_index

    def get_avail_moves(self) -> set[Disks]:
        result: set[Disks] = set()
        for index, node in enumerate(self):
            used = node[0]
            if used == 0:
                continue
            for nei_index in self.neis[index]:
                nei = self[nei_index]
                if used <= nei[1]:
                    # print(f"node = [{index}]{node} -> nei = [{nei_index}]{nei}")
                    result.add(self.move(index, nei_index))
        return result

    def move(self, source: int, target: int) -> Disks:
        source_node = self[source]
        target_node = self[target]
        if source_node[0] == 0:
            print(f"source_node = {source_node} target_node = {target_node}")
            raise NotImplementedError
        if source_node[0] > target_node[1]:
            print(f"source_node = {source_node} target_node = {target_node}")
            raise NotImplementedError
        if source < target:
            data = (
                self[:source]
                + ((0, source_node[0] + source_node[1]),)
                + self[source + 1 : target]
                + ((target_node[0] + source_node[0], target_node[1] - source_node[0]),)
                + self[target + 1 :]
            )
        elif source > target:
            data = (
                self[:target]
                + ((target_node[0] + source_node[0], target_node[1] - source_node[0]),)
                + self[target + 1 : source]
                + ((0, source_node[0] + source_node[1]),)
                + self[source + 1 :]
            )
        else:
            raise NotImplementedError
        if source == self.source_index:
            source_index = target
        else:
            source_index = self.source_index
        return Disks(data, source_index, self.target_index, self.neis)


def generate_disks(
    nodes: dict[tuple[int, int], tuple[int, int]],
    source_node: tuple[int, int],
    target_node: tuple[int, int],
) -> Disks:
    keys: list[tuple[int, int]] = sorted(nodes.keys())
    data: list[tuple[int, int]] = []
    for key in keys:
        data.append(nodes[key])
    neis: dict[int, set[int]] = dict()
    for index1, key1 in enumerate(keys):
        x1, y1 = key1
        if index1 not in neis:
            neis[index1] = set()
        for dx, dy in [(0, 1), (1, 0)]:
            x2 = x1 + dx
            y2 = y1 + dy
            if (x2, y2) not in keys:
                continue
            index2 = keys.index((x2, y2))
            if index2 not in neis:
                neis[index2] = set()
            neis[index1].add(index2)
            neis[index2].add(index1)
    source_index = keys.index(source_node)
    target_index = keys.index(target_node)
    return Disks(data, source_index, target_index, neis)


def dist(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main() -> None:
    # nodes: dict[tuple[int, int], tuple[int, int]] = dict()
    nodes: list[list[tuple[int, int]]] = []
    big_nodes: set[tuple[int, int]] = set()
    small_nodes: set[tuple[int, int]] = set()
    empty_nodes: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.search(
                r"node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+\%", line
            )
            if line_match is None:
                print(f"skipped line: {line.strip()}")
            else:
                key = (int(line_match.group(1)), int(line_match.group(2)))
                if key[0] == len(nodes):
                    nodes.append([])
                if key[1] != len(nodes[-1]):
                    raise NotImplementedError
                nodes[-1].append((int(line_match.group(3)), int(line_match.group(4))))
                if nodes[-1][-1][0] == 0:
                    empty_nodes.add(key)
                if nodes[-1][-1][0] > SMALL_VS_BIG:
                    big_nodes.add(key)
                else:
                    small_nodes.add(key)
    target_node = (0, 0)
    source_node = (len(nodes) - 1, 0)
    print(f"source_node = {source_node}")
    print(f"target_node = {target_node}")
    print(f"empty_nodes = {empty_nodes}")
    print(f"big_nodes = {big_nodes}")
    # print(f"small_nodes = {small_nodes}")
    # find max free space on big_nodes
    max_free_on_big = 0
    for x, y in big_nodes:
        max_free_on_big = max(max_free_on_big, nodes[x][y][1])
    # find max free space on small nodes
    # find max used space on small nodes
    max_free_on_small = 0
    min_used_on_small = None
    for x, y in small_nodes:
        if nodes[x][y][0] == 0:
            continue
        max_free_on_small = max(max_free_on_small, nodes[x][y][1])
        if min_used_on_small is None or min_used_on_small > nodes[x][y][0]:
            min_used_on_small = nodes[x][y][0]
    if max_free_on_big >= min_used_on_small:
        print(f"max_free_on_big = {max_free_on_big} >= {min_used_on_small}")
        raise NotImplementedError
    if max_free_on_small >= min_used_on_small:
        print(
            f"max_free_on_big = {max_free_on_small} >= {min_used_on_small} = min_used_on_small"
        )
        raise NotImplementedError
    if len(empty_nodes) != 1:
        raise NotImplementedError
    # verified limitations
    empty_node = empty_nodes.pop()
    Q = {
        (
            0,
            # dist(empty_node, source_node),
            # dist(target_node, source_node),
            empty_node,
            source_node,
        )
    }
    paths = {(empty_node, source_node): []}
    prev_steps = 0
    win_steps = 100500
    while len(Q) > 0:
        current = min(Q)
        Q.remove(current)
        # print(f"current = {current} len(Q) = {len(Q)}")
        # print(f"current = {current} len(Q) = {len(Q)} visited = {visited}")
        steps, current_empty, current_source = current
        if current_source == target_node:
            print(paths[current_empty,current_source])
            break
        # steps, _, _, current_empty, current_source = current
        if steps != prev_steps:
            prev_steps = steps
            print(f"current = {current} len(Q) = {len(Q)}")
        if steps > win_steps:
            break
        for dx, dy in DIRECTIONS:
            x = current_empty[0] + dx
            y = current_empty[1] + dy
            new_empty = (x, y)
            if new_empty not in small_nodes:
                continue
            if new_empty == current_source:
                if current_empty == target_node:
                    print(f"Found it {steps+1}")
                    win_steps = steps + 1
                    # return
                new_visited = (current_source, current_empty)
                if new_visited in paths:
                    continue
                paths[new_visited] = paths[current_empty,current_source]+[((x,y),(current_source))]
                Q.add(
                    (
                        steps + 1,
                        # dist(current_source, current_empty),
                        # dist(target_node, current_source),
                        current_source,
                        current_empty,
                    )
                )
            else:
                new_visited = (new_empty, current_source)
                if new_visited in paths:
                    continue
                paths[new_visited] = paths[current_empty,current_source]+[((x,y),(current_source))]
                Q.add(
                    (
                        steps + 1,
                        # dist(new_empty, current_source),
                        # dist(target_node, new_empty),
                        new_empty,
                        current_source,
                    )
                )

    return
    y = 0
    while (0, y) in nodes.keys():
        x = 0
        while (x, y) in nodes.keys():
            print(f"{nodes[x,y][0]:>3}/{nodes[x,y][1]:<3}", end="")
            if (x, y) == source_node:
                directions == "!"
            else:
                directions = ""
            if nodes[x, y][0] == 0:
                directions += "    "
            else:
                if (x, y - 1) in nodes and nodes[x, y][0] <= nodes[x, y - 1][1]:
                    directions += "^"
                else:
                    directions += " "
                if (x, y + 1) in nodes and nodes[x, y][0] <= nodes[x, y + 1][1]:
                    directions += "v"
                else:
                    directions += " "
                if (x - 1, y) in nodes and nodes[x, y][0] <= nodes[x - 1, y][1]:
                    directions += "<"
                else:
                    directions += " "
                if (x + 1, y) in nodes and nodes[x, y][0] <= nodes[x + 1, y][1]:
                    directions += ">"
                else:
                    directions += " "
            print(directions, end="|")
            x += 1
        print()
        y += 1
    return
    start_state = generate_disks(nodes, source_node, target_node)
    # print(start_state)
    Q = [(0, start_state)]
    visited = {start_state}
    prev_steps = 0
    while len(Q) > 0:
        steps, current_state = Q.pop(0)
        if steps != prev_steps:
            print("!", steps, len(Q), len(visited))
            prev_steps = steps
        for new_state in current_state.get_avail_moves():
            if new_state.is_ready:
                print(f"steps = {steps+1}")
                print("\n".join(map(str, sorted(visited))))
                return
            if new_state in visited:
                continue
            visited.add(new_state)
            Q.append((steps + 1, new_state))


if __name__ == "__main__":
    main()
