from __future__ import annotations
from collections.abc import Iterator
import re

FILENAME = "demo.txt"  # expected 1651
FILENAME = "input.txt"

TIME = 30
START = "AA"


def generate_flow(
    valves: dict[str, int],
    paths: dict[str, dict[str, int]],
    start: str = START,
    time_left: int = 30,
    exclude: set[str] | None = None,
    add_value: int = 0,
) -> Iterator[int]:
    if time_left == 0:
        yield add_value
        return
    if exclude is None:
        exclude = set()
        for key, value in valves.items():
            if value == 0:
                exclude.add(key)
    if len(valves) == len(exclude):
        yield add_value
        return
    if start not in exclude:
        yield from generate_flow(
            valves,
            paths,
            start,
            time_left - 1,
            exclude.union({start}),
            add_value + valves[start] * (time_left - 1),
        )
    else:
        next_valves = set(paths[start].keys()).difference(exclude)
        for next_valve in next_valves:
            if time_left > paths[start][next_valve]:
                yield from generate_flow(
                    valves,
                    paths,
                    next_valve,
                    time_left - paths[start][next_valve],
                    exclude,
                    add_value,
                )


def main() -> None:
    valves: dict[str, int] = dict()
    paths: dict[str, dict[str, int]] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]+)",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            valves[line_match.group(1)] = int(line_match.group(2))
            paths[line_match.group(1)] = dict()
            for item in line_match.group(3).split(", "):
                paths[line_match.group(1)][item] = 1
    print(valves)
    Q: set[str] = set(valves.keys())
    while len(Q) > 0:
        valve0 = Q.pop()
        is_changed = False
        for valve1, dist1 in paths[valve0].items():
            for valve2, dist2 in paths[valve1].items():
                if valve2 == valve0:
                    continue
                if valve2 not in paths[valve0] or paths[valve0][valve2] > dist1 + dist2:
                    paths[valve0][valve2] = dist1 + dist2
                    Q.add(valve0)
                    is_changed = True
                    break
            if is_changed:
                break
    result = None
    for flow in generate_flow(valves, paths):
        if result is None or flow > result:
            result = flow
    print(result)


if __name__ == "__main__":
    main()
