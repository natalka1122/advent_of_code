from __future__ import annotations
import random

FILENAME = "demo.txt"
FILENAME = "input.txt"
THREE = 3


class Edge:
    def __init__(self, v1: str, v2: str) -> None:
        if v1 == v2:
            print(f"v1 = {v1} v2 = {v2}")
            raise NotImplementedError
        if v2 < v1:
            v1, v2 = v2, v1
        self._v1 = v1
        self._v2 = v2
        self.name = f"['{v1}_{v2}']"

    def __repr__(self) -> str:
        return f"{self.name} {self._v1,self._v2}"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Edge) and self.tuple == other.tuple

    def _set_v1(self, value: str) -> None:
        if self._v2 == value:
            print(f"set_v1: self = {self} value = {value}")
            raise NotImplementedError
        self._v1 = value
        if self._v1 > self._v2:
            self._v1, self._v2 = self._v2, self._v1

    def _set_v2(self, value: str) -> None:
        if self._v1 == value:
            print(f"set_v2: self = {self} value = {value}")
            raise NotImplementedError
        self._v2 = value
        if self._v1 > self._v2:
            self._v1, self._v2 = self._v2, self._v1

    def copy(self) -> Edge:
        return Edge(self._v1, self._v2)

    @property
    def tuple(self) -> tuple[str, str]:
        return self._v1, self._v2

    def not_vertex(self, vertex: str) -> str:
        if vertex == self._v1:
            return self._v2
        if vertex == self._v2:
            return self._v1
        print(f"not_vertex: self = {self} vertex = {vertex}")
        raise NotImplementedError

    def replace(self, before: str, after: str, fail: bool) -> None:
        if before == after:
            print(f"replace: self = {self} before = {before} after = {after}")
            raise NotImplementedError
        if self._v1 == before:
            self._set_v1(after)
        elif self._v2 == before:
            self._set_v2(after)
        elif fail:
            print(f"replace: self = {self} before = {before} after = {after}")
            raise NotImplementedError


def check(graph: dict[str, list[Edge]]) -> bool:
    for v1 in graph:
        for edge in graph[v1]:
            if v1 not in edge.tuple:
                print(f"Case 1: {v1} not in {edge}")
                print(graph)
                return False
            v2 = edge.not_vertex(v1)
            if v2 not in graph:
                print(f"Case 2: {v2} not in graph")
                print(graph)
                return False
            if edge not in graph[v2]:
                print(f"Case 3: Edge {edge} not in graph[{v2}]")
                print(graph)
                return False
    return True


def karger_min_cut(graph0: dict[str, list[Edge]]) -> tuple[int, list[int]]:
    """
    Implements Karger's algorithm to find the minimum cut of a graph.

    Parameters:
        graph (dict): A dictionary where keys are nodes and values are lists of nodes
                      that the key node is connected to (adjacency list).

    Returns:
        int: The size of the minimum cut.
    """
    # Create a deepcopy of the graph to avoid modifying the original
    graph: dict[str, list[Edge]] = dict()
    for v in graph0:
        graph[v] = []
        for edge in graph0[v]:
            graph[v].append(edge.copy())
    history: dict[str, set[str]] = dict()
    while len(graph) > 2:
        if not check(graph):
            raise NotImplementedError
        # Randomly select an edge (u, v)
        target: str = random.choice(list(graph.keys()))
        to_remove_edge: Edge = random.choice(graph[target])
        to_remove: str = to_remove_edge.not_vertex(target)
        if target not in history:
            history[target] = {target}
        if to_remove not in history:
            history[to_remove] = {to_remove}
        history[target].update(history[to_remove])
        # print(f"Merge {to_remove} into {target} to_remove_edge = {to_remove_edge}")

        # Merge node v into node u
        while to_remove_edge in graph[target]:
            graph[target].remove(to_remove_edge)
        for edge in graph[to_remove]:
            if edge == to_remove_edge:
                continue
            # Redirect all edges pointing to v to point to u
            vertex = edge.not_vertex(to_remove)
            for edge1 in graph[vertex]:
                edge1.replace(to_remove, target, fail=False)

            # Add all edges of v to u, excluding self-loops
            edge.replace(to_remove, target, fail=True)
            graph[target].append(edge)
        for edge in graph[to_remove]:
            if edge == to_remove_edge:
                continue

        # Remove v from the graph
        del graph[to_remove]

    # The graph now has exactly two nodes; the edges between them form the cut
    if len(graph) != 2:
        raise NotImplementedError
    subnets_size: list[int] = []
    for key in graph.keys():
        if key not in history:
            subnets_size.append(0)
        else:
            subnets_size.append(len(history[key]))
    remaining_edges = list(graph.values())[0]
    return len(remaining_edges), subnets_size


def main() -> None:
    edges: dict[str, list[Edge]] = dict()
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(": ")
            left = line[0]
            right = line[1].split(" ")
            if left not in edges:
                edges[left] = []
            for item in right:
                if item not in edges:
                    edges[item] = []
                edge = Edge(left, item)
                edges[left].append(edge)
                edges[item].append(edge)
    print(edges)
    print(len(edges))

    min_cut = None
    while True:
        cut = karger_min_cut(edges)
        print(cut[0])
        if min_cut is None or min_cut[0] > cut[0]:
            min_cut = cut
            if min_cut[0] == THREE:
                break
    print(f"min_cut = {min_cut}")
    result = 1
    for subnet_size in min_cut[1]:
        result *= subnet_size
    print(result)


if __name__ == "__main__":
    main()
