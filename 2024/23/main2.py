from typing import Iterator
import re

# FILENAME = "demo.txt"  # expected co,de,ka,ta
FILENAME = "input.txt"


def BronKerbosch1(
    R: set[str],
    P: set[str],
    X: set[str],
    the_map: dict[str, set[str]],
) -> Iterator[set[str]]:
    if len(P) == 0 and len(X) == 0:
        # print(f"return {R}")
        yield R
    for v in P:
        yield from BronKerbosch1(
            R.union({v}),
            P.intersection(the_map[v]),
            X.intersection(the_map[v]),
            the_map,
        )
        P = P - {v}
        X = X.union({v})


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
    best_cluqie: set[str] = set()
    for cliqie in BronKerbosch1(set(), set(the_map.keys()), set(), the_map):
        if len(cliqie) > len(best_cluqie):
            best_cluqie = cliqie
    print(",".join(sorted(best_cluqie)))


if __name__ == "__main__":
    main()
