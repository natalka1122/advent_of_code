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
    path0: list[str] | None = None,
    path1: list[str] | None = None,
) -> Iterator[tuple[int, list[str], list[str], str]]:
    if time_left < 0:
        raise NotImplementedError
    if time_left == 0:
        if path0 is None or path1 is None:
            raise NotImplementedError
        raise NotImplementedError
        yield add_value, path0, path1, "case 01"
        return
    if exclude is None:
        exclude = set()
        for key, value in valves.items():
            if value == 0:
                exclude.add(key)
    if start is None:
        start = (START, START)
    if on_path is None:
        on_path = (0, 0)
    if path0 is None:
        path0 = []
    if path1 is None:
        path1 = []
    # This uses the fact that flow from START is 0
    if start[0] not in exclude:
        print(f"path0 = {path0} path1 = {path1}")
        raise NotImplementedError
    if start[1] not in exclude:
        print(f"path0 = {path0} path1 = {path1}")
        raise NotImplementedError
    # if len(valves) == len(exclude):
    #     yield add_value, path0, path1, "case 02"
    #     return
    possible_path0 = set(paths[start[0]]).difference(exclude)
    possible_path0 = possible_path0.difference(start)
    possible_path1 = set(paths[start[1]]).difference(exclude)
    possible_path1 = possible_path1.difference(start)
    if possible_path0 != possible_path1:
        raise NotImplementedError
    possible_path = possible_path0
    possible_path_sorted = sorted(possible_path)
    if on_path == (0, 0):
        if len(possible_path_sorted) == 0:
            yield add_value, path0, path1, "case 10"
        for next_valve0 in possible_path_sorted:
            if next_valve0 in start:
                raise NotImplementedError
            for next_valve1 in possible_path_sorted:
                if next_valve0 == next_valve1:
                    continue
                if start[0] == start[1] and next_valve0 > next_valve1:
                    continue
                if next_valve1 in start:
                    raise NotImplementedError
                min_path = min(
                    paths[start[0]][next_valve0], paths[start[1]][next_valve1]
                )
                max_path = max(
                    paths[start[0]][next_valve0], paths[start[1]][next_valve1]
                )
                if time_left < max_path:
                    raise NotImplementedError
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
                    path0=path0
                    + [
                        next_valve0,
                        f"case 11: {valves[next_valve0] * (time_left - paths[start[0]][next_valve0])}",
                    ],
                    path1=path1
                    + [
                        next_valve1,
                        f"case 11: {valves[next_valve1] * (time_left - paths[start[1]][next_valve1])}",
                    ],
                )
    # elif start[0] in exclude and start[1] not in exclude:
    #     if len(possible_path_sorted) == 0:
    #         yield add_value + valves[start[1]] * (
    #             time_left - 1
    #         ), path0, path1, "case 11"
    #     for next_valve0 in possible_path_sorted:
    #         if next_valve0 in start:
    #             raise NotImplementedError
    #         if time_left < paths[start[0]][next_valve0]:
    #             raise NotImplementedError
    #         yield from generate_flow(
    #             valves,
    #             paths,
    #             start=(next_valve0, start[1]),
    #             on_path=(paths[start[0]][next_valve0] - 1, 0),
    #             time_left=time_left - 1,
    #             exclude=exclude.union({start[1]}),
    #             add_value=add_value + valves[start[1]] * (time_left - 1),
    #             path0=path0 + [next_valve0],
    #             path1=path1,
    #         )
    # elif start[0] not in exclude and start[1] in exclude:
    #     if len(possible_path_sorted) == 0:
    #         yield add_value + valves[start[0]] * (
    #             time_left - 1
    #         ), path0, path1, "case 11"
    #     for next_valve1 in possible_path_sorted:
    #         if next_valve1 in start:
    #             raise NotImplementedError
    #         if time_left < paths[start[1]][next_valve1]:
    #             print(f"path0 = {path0} path1 = {path1}")
    #             raise NotImplementedError
    #         yield from generate_flow(
    #             valves,
    #             paths,
    #             start=(start[0], next_valve1),
    #             on_path=(0, paths[start[1]][next_valve1] - 1),
    #             time_left=time_left - 1,
    #             exclude=exclude.union({start[0]}),
    #             add_value=add_value + valves[start[0]] * (time_left - 1),
    #             path0=path0,
    #             path1=path1 + [next_valve1],
    #         )
    # elif start[0] not in exclude and start[1] not in exclude:
    #     yield from generate_flow(
    #         valves,
    #         paths,
    #         start=start,
    #         on_path=(0, 0),
    #         time_left=time_left - 1,
    #         exclude=exclude.union({start[0], start[1]}),
    #         add_value=add_value
    #         + valves[start[0]] * (time_left - 1)
    #         + valves[start[1]] * (time_left - 1),
    #         path0=path0,
    #         path1=path1,
    #     )
    # else:
    #     raise NotImplementedError
    elif on_path[0] == 0 and on_path[1] > 0:
        # if start[0] in exclude:
        if len(possible_path_sorted) == 0:
            yield from generate_flow(
                valves,
                paths,
                start=start,
                on_path=(0, 0),
                time_left=time_left - on_path[1],
                exclude=exclude,
                add_value=add_value,
                path0=path0 + ["case 20"],
                path1=path1,
            )
        for next_valve0 in possible_path_sorted:
            if next_valve0 in start:
                raise NotImplementedError
            if time_left < paths[start[0]][next_valve0]:
                raise NotImplementedError
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
                path0=path0
                + [
                    next_valve0,
                    f"case 21: {valves[next_valve0] * (time_left - paths[start[0]][next_valve0])}",
                ],
                path1=path1,
            )
    # else:
    #     raise NotImplementedError
    #     # yield from generate_flow(
    #     #     valves,
    #     #     paths,
    #     #     start=start,
    #     #     on_path=(0, on_path[1] - 1),
    #     #     time_left=time_left - 1,
    #     #     exclude=exclude.union({start[0]}),
    #     #     add_value=add_value + valves[start[0]] * (time_left - 1),
    #     #     path0=path0,
    #     #     path1=path1,
    #     # )
    elif on_path[1] == 0 and on_path[0] > 0:
        # if start[1] in exclude:
        if len(possible_path_sorted) == 0:
            yield from generate_flow(
                valves,
                paths,
                start=start,
                on_path=(0, 0),
                time_left=time_left - on_path[0],
                exclude=exclude,
                add_value=add_value,
                path0=path0,
                path1=path1 + ["case 30"],
            )
        for next_valve1 in possible_path_sorted:
            if next_valve1 in start:
                raise NotImplementedError
            if time_left < paths[start[1]][next_valve1]:
                print(f"path0 = {path0} path1 = {path1}")
                raise NotImplementedError
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
                path0=path0,
                path1=path1
                + [
                    next_valve1,
                    f"case 31: {valves[next_valve1] * (time_left - paths[start[1]][next_valve1])}",
                ],
            )
    # else:
    #     raise NotImplementedError
    #     yield from generate_flow(
    #         valves,
    #         paths,
    #         start=start,
    #         on_path=(on_path[0] - 1, 0),
    #         time_left=time_left - 1,
    #         exclude=exclude.union({start[1]}),
    #         add_value=add_value + valves[start[1]] * (time_left - 1),
    #         path0=path0,
    #         path1=path1,
    #     )
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
        print(flow)
        if result is None or flow[0] > result[0]:
            result = flow
    print(result)


if __name__ == "__main__":
    main()
