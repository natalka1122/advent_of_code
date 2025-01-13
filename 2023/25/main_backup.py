from __future__ import annotations
import random

FILENAME = "demo.txt"
# FILENAME = "input.txt"


# Karger's algorithm to find Minimum Cut in an
# undirected, unweighted and connected graph.


# a class to represent a unweighted edge in graph
class Edge:
    def __init__(self, s, d):
        self.src = s
        self.dest = d

    def __repr__(self):
        return str((self.src, self.dest))


# a class to represent a connected, undirected
# and unweighted graph as a collection of edges.
class Graph:

    # V-> Number of vertices, E-> Number of edges
    def __init__(self, v, e):
        self.V = v
        self.E = e

        # graph is represented as an array of edges.
        # Since the graph is undirected, the edge
        # from src to dest is also edge from dest
        # to src. Both are counted as 1 edge here.
        self.edge = []


# A class to represent a subset for union-find
class subset:
    def __init__(self, p, r):
        self.parent = p
        self.rank = r

    def __repr__(self):
        return str((self.parent, self.rank))


# A very basic implementation of Karger's randomized
# algorithm for finding the minimum cut. Please note
# that Karger's algorithm is a Monte Carlo Randomized algo
# and the cut returned by the algorithm may not be
# minimum always
def kargerMinCut(graph):

    # Get data of given graph
    V = graph.V
    E = graph.E
    edge = graph.edge

    # Allocate memory for creating V subsets.
    subsets = []

    # Create V subsets with single elements
    for v in range(V):
        subsets.append(subset(v, 0))

    # Initially there are V vertices in
    # contracted graph
    vertices = V

    # Keep contracting vertices until there are
    # 2 vertices.
    while vertices > 2:

        # Pick a random edge
        i = int(10 * random.random()) % E

        # Find vertices (or sets) of two corners
        # of current edge
        subset1 = find(subsets, edge[i].src)
        subset2 = find(subsets, edge[i].dest)

        # If two corners belong to same subset,
        # then no point considering this edge
        if subset1 == subset2:
            print(
                f"vertices = {vertices} subset1 = {type(subset1)} {subset1} subset2 = {subset2} subsets = {subsets}"
            )
            continue

        # Else contract the edge (or combine the
        # corners of edge into one vertex)
        else:
            print("Contracting edge " + str(edge[i].src) + "-" + str(edge[i].dest))
            vertices -= 1
            Union(subsets, subset1, subset2)

    # Now we have two vertices (or subsets) left in
    # the contracted graph, so count the edges between
    # two components and return the count.
    cutedges = 0
    for i in range(E):
        subset1 = find(subsets, edge[i].src)
        subset2 = find(subsets, edge[i].dest)
        if subset1 != subset2:
            cutedges += 1

    return cutedges


# A utility function to find set of an element i
# (uses path compression technique)


def find(subsets, i):

    # find root and make root as parent of i
    # (path compression)
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)

    return subsets[i].parent


# A function that does union of two sets of x and y
# (uses union by rank)
def Union(subsets, x, y):
    xroot = find(subsets, x)
    yroot = find(subsets, y)

    # Attach smaller rank tree under root of high
    # rank tree (Union by Rank)
    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot

    # If ranks are same, then make one as root and
    # increment its rank by one
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1


def main():
    vertex: list[str] = []
    edges: set[tuple[int, int]] = set()
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(": ")
            left = line[0]
            right = line[1].split(" ")
            if left not in vertex:
                vertex.append(left)
            for item in right:
                if item not in vertex:
                    vertex.append(item)
                if item < left:
                    edges.add((vertex.index(item), vertex.index(left)))
                elif left < item:
                    edges.add((vertex.index(left), vertex.index(item)))
                else:
                    raise NotImplementedError
    print(edges)
    print(len(edges))
    graph = Graph(len(vertex), len(edges))
    for e1, e2 in edges:
        graph.edge.append(Edge(e1, e2))
    print("do it")
    r = random.random()
    res = kargerMinCut(graph)
    print("Cut found by Karger's randomized algo is", res)


if __name__ == "__main__":
    main()
