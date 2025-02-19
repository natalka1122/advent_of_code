from __future__ import annotations
from collections.abc import Iterator
import re

FILENAME = "demo.txt"  # expected 1707
# FILENAME = "input.txt"

TIME = 26
START = "AA"


def generate_flow(
    valves: dict[str, int],
    paths: dict[str, dict[str, int]],
    start: tuple[str, str] | None = None,
    on_path: tuple[int, int] | None = None,
    time_left: int = TIME,
    exclude: set[str] | None = None,
    add_value: int = 0,
) -> Iterator[int]:
    if time_left < 0:
        raise NotImplementedError
    if time_left == 0:
        if on_path == (0, 0):
            yield add_value
            return
        print(f"on_path = {on_path}")
        raise NotImplementedError
    if exclude is None:
        exclude = set()
        for key, value in valves.items():
            if value == 0:
                exclude.add(key)
    if start is None:
        start = (START, START)
    if on_path is None:
        on_path = (0, 0)
    # Use the fact that flow from START is 0
    if start[0] not in exclude:
        raise NotImplementedError
    if start[1] not in exclude:
        raise NotImplementedError
    possible_path = set(paths[start[0]]).difference(exclude)
    if on_path == (0, 0):
        if len(possible_path) == 0:
            yield add_value
        cannot_go_anywhere0 = True
        for next_valve0 in possible_path:
            if time_left < paths[start[0]][next_valve0]:
                continue
            if time_left == TIME:
                print(next_valve0)
            cannot_go_anywhere0 = False
            cannot_go_anywhere1 = True
            for next_valve1 in possible_path:
                if next_valve0 == next_valve1:
                    continue
                if start[0] == start[1] and next_valve0 > next_valve1:
                    continue
                if time_left < paths[start[1]][next_valve1]:
                    continue
                cannot_go_anywhere1 = False
                min_path = min(
                    paths[start[0]][next_valve0], paths[start[1]][next_valve1]
                )
                yield from generate_flow(
                    valves,
                    paths,
                    start=(next_valve0, next_valve1),
                    on_path=(
                        paths[start[0]][next_valve0] - min_path,
                        paths[start[1]][next_valve1] - min_path,
                    ),
                    time_left=time_left - min_path,
                    exclude=exclude.union({next_valve0, next_valve1}),
                    add_value=add_value
                    + valves[next_valve0] * (time_left - paths[start[0]][next_valve0])
                    + valves[next_valve1] * (time_left - paths[start[1]][next_valve1]),
                )
            if cannot_go_anywhere1:
                yield from generate_flow(
                    valves,
                    paths,
                    start=(next_valve0, start[1]),
                    on_path=(0, 0),
                    time_left=time_left - paths[start[0]][next_valve0],
                    exclude=exclude.union({next_valve0}),
                    add_value=add_value
                    + valves[next_valve0] * (time_left - paths[start[0]][next_valve0]),
                )
        if cannot_go_anywhere0:
            cannot_go_anywhere1 = True
            for next_valve1 in possible_path:
                if time_left < paths[start[1]][next_valve1]:
                    continue
                cannot_go_anywhere1 = False
                yield from generate_flow(
                    valves,
                    paths,
                    start=(start[0], next_valve1),
                    on_path=(0, 0),
                    time_left=time_left - paths[start[1]][next_valve1],
                    exclude=exclude.union({next_valve1}),
                    add_value=add_value
                    + valves[next_valve1] * (time_left - paths[start[1]][next_valve1]),
                )
            if cannot_go_anywhere1:
                yield add_value
    elif on_path[0] == 0 and on_path[1] > 0:
        if len(possible_path) == 0:
            yield from generate_flow(
                valves,
                paths,
                start=start,
                on_path=(0, 0),
                time_left=time_left - on_path[1],
                exclude=exclude,
                add_value=add_value,
            )
        cannot_go_anywhere = True
        for next_valve0 in possible_path:
            if time_left < paths[start[0]][next_valve0]:
                continue
            cannot_go_anywhere = False
            min_path = min(paths[start[0]][next_valve0], on_path[1])
            yield from generate_flow(
                valves,
                paths,
                start=(next_valve0, start[1]),
                on_path=(
                    paths[start[0]][next_valve0] - min_path,
                    on_path[1] - min_path,
                ),
                time_left=time_left - min_path,
                exclude=exclude.union({next_valve0}),
                add_value=add_value
                + valves[next_valve0] * (time_left - paths[start[0]][next_valve0]),
            )
        if cannot_go_anywhere:
            yield from generate_flow(
                valves,
                paths,
                start=start,
                on_path=(0, 0),
                time_left=time_left - on_path[1],
                exclude=exclude,
                add_value=add_value,
            )
    elif on_path[1] == 0 and on_path[0] > 0:
        if len(possible_path) == 0:
            yield from generate_flow(
                valves,
                paths,
                start=start,
                on_path=(0, 0),
                time_left=time_left - on_path[0],
                exclude=exclude,
                add_value=add_value,
            )
        cannot_go_anywhere = True
        for next_valve1 in possible_path:
            if time_left < paths[start[1]][next_valve1]:
                continue
            cannot_go_anywhere = False
            min_path = min(paths[start[1]][next_valve1], on_path[0])
            yield from generate_flow(
                valves,
                paths,
                start=(start[0], next_valve1),
                on_path=(
                    on_path[0] - min_path,
                    paths[start[1]][next_valve1] - min_path,
                ),
                time_left=time_left - min_path,
                exclude=exclude.union({next_valve1}),
                add_value=add_value
                + valves[next_valve1] * (time_left - paths[start[1]][next_valve1]),
            )
        if cannot_go_anywhere:
            yield from generate_flow(
                valves,
                paths,
                start=start,
                on_path=(0, 0),
                time_left=time_left - on_path[0],
                exclude=exclude,
                add_value=add_value,
            )
    else:
        print(f"on_path = {on_path}")
        raise NotImplementedError


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
    # Add one for opening the valve
    for valve0 in paths:
        for valve1 in paths[valve0]:
            paths[valve0][valve1] += 1
    # print(paths)
    result = None
    for flow in generate_flow(valves, paths):
        if result is None or flow > result:
            result = flow
    print(result)


if __name__ == "__main__":
    main()
