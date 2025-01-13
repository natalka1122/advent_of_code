from typing import Optional
import functools
import re

# FILENAME, DEPTH = "demo.txt", 2  # expected 126384
# FILENAME, DEPTH = "demo.txt", 25  # expected 154115708116294
FILENAME, DEPTH = "input.txt", 25
A = "A"
LEFT = "<"
RIGHT = ">"
UP = "^"
DOWN = "v"
DIGITS = "1234567890A"
DIRECTIONS = "^<>vA"
INF = 100500


@functools.cache
def do_numerical(state: str, arrow: str) -> Optional[str]:
    if state not in DIGITS:
        raise NotImplementedError
    if arrow not in DIRECTIONS:
        raise NotImplementedError
    result = {
        ("7", RIGHT): "8",
        ("7", DOWN): "4",
        ("8", LEFT): "7",
        ("8", DOWN): "5",
        ("8", RIGHT): "9",
        ("9", LEFT): "8",
        ("9", DOWN): "6",
        ("4", UP): "7",
        ("4", RIGHT): "5",
        ("4", DOWN): "1",
        ("5", UP): "8",
        ("5", LEFT): "4",
        ("5", RIGHT): "6",
        ("5", DOWN): "2",
        ("6", UP): "9",
        ("6", LEFT): "5",
        ("6", DOWN): "3",
        ("1", UP): "4",
        ("1", RIGHT): "2",
        ("2", UP): "5",
        ("2", LEFT): "1",
        ("2", RIGHT): "3",
        ("2", DOWN): "0",
        ("3", UP): "6",
        ("3", LEFT): "2",
        ("3", DOWN): "A",
        ("0", UP): "2",
        ("0", RIGHT): "A",
        ("A", UP): "3",
        ("A", LEFT): "0",
    }
    if (state, arrow) in result:
        return result[(state, arrow)]
    return None


@functools.cache
def do_directional(state: str, arrow: str) -> Optional[str]:
    if state not in DIRECTIONS:
        raise NotImplementedError
    if arrow not in DIRECTIONS:
        raise NotImplementedError
    result = {
        (UP, RIGHT): A,
        (UP, DOWN): DOWN,
        (A, LEFT): UP,
        (A, DOWN): RIGHT,
        (LEFT, RIGHT): DOWN,
        (DOWN, UP): UP,
        (DOWN, LEFT): LEFT,
        (DOWN, RIGHT): RIGHT,
        (RIGHT, UP): A,
        (RIGHT, LEFT): DOWN,
    }
    if (state, arrow) in result:
        return result[(state, arrow)]
    return None


def find_all_numerical_paths() -> dict[tuple[str, str], tuple[int, set[str]]]:
    paths: dict[tuple[str, str], tuple[int, set[str]]] = dict()
    for start in DIGITS:
        if (start, start) in paths:
            raise NotImplementedError
        paths[(start, start)] = 0, {""}
        Q = {start}
        while len(Q) > 0:
            current = Q.pop()
            for button in DIRECTIONS:
                if button == A:
                    continue
                button_apply = do_numerical(current, button)
                if button_apply is None:
                    continue
                if (start, button_apply) not in paths or paths[(start, button_apply)][
                    0
                ] > paths[(start, current)][0] + 1:
                    paths[(start, button_apply)] = paths[(start, current)][0] + 1, set()
                if paths[(start, button_apply)][0] >= paths[(start, current)][0] + 1:
                    for current_path in paths[(start, current)][1]:
                        paths[(start, button_apply)][1].add(current_path + button)
                    Q.add(button_apply)
    new_paths: dict[tuple[str, str], tuple[int, set[str]]] = dict()
    for pair in paths:
        new_paths[pair] = paths[pair][0] + 1, set()
        for path in paths[pair][1]:
            new_paths[pair][1].add(path + A)
    return new_paths


def find_all_directional_paths() -> dict[tuple[str, str], tuple[int, set[str]]]:
    paths: dict[tuple[str, str], tuple[int, set[str]]] = dict()
    for start in DIRECTIONS:
        if (start, start) in paths:
            raise NotImplementedError
        paths[(start, start)] = 0, {""}
        Q = {start}
        while len(Q) > 0:
            current = Q.pop()
            for button in DIRECTIONS:
                if button == A:
                    continue
                button_apply = do_directional(current, button)
                if button_apply is None:
                    continue
                if (start, button_apply) not in paths:
                    paths[(start, button_apply)] = INF, set()
                if paths[(start, button_apply)][0] > paths[(start, current)][0] + 1:
                    paths[(start, button_apply)] = paths[(start, current)][0] + 1, set()
                if paths[(start, button_apply)][0] >= paths[(start, current)][0] + 1:
                    for current_path in paths[(start, current)][1]:
                        paths[(start, button_apply)][1].add(current_path + button)
                    Q.add(button_apply)
    new_paths: dict[tuple[str, str], tuple[int, set[str]]] = dict()
    for pair in paths:
        new_paths[pair] = paths[pair][0] + 1, set()
        for path in paths[pair][1]:
            new_paths[pair][1].add(path + A)
    return new_paths


all_numerical_paths = find_all_numerical_paths()
all_directional_paths = find_all_directional_paths()


@functools.cache
def calc_directional(source: str, target: str, depth: int) -> int:
    if depth < 0:
        raise NotImplementedError
    if depth == 1:
        return all_directional_paths[(source, target)][0]
    result = None
    for path in all_directional_paths[(source, target)][1]:
        current = 0
        start = A
        for symbol in path:
            current += calc_directional(start, symbol, depth - 1)
            start = symbol
        if result is None or current < result:
            result = current
    if result is None:
        raise NotImplementedError
    return result


@functools.cache
def calc_numeric(source: str, target: str, depth: int) -> int:
    if depth < 0:
        raise NotImplementedError
    if depth == 0:
        if (source, target) in all_numerical_paths:
            return all_numerical_paths[(source, target)][0]
    result = None
    for path in all_numerical_paths[(source, target)][1]:
        start1 = A
        current = 0
        for symbol in path:
            current += calc_directional(start1, symbol, depth)
            start1 = symbol
        if result is None or current < result:
            result = current
    if result is None:
        raise NotImplementedError
    return result


def f(line: str) -> int:
    result = 0
    start = A
    for symbol in line:
        result += calc_numeric(start, symbol, depth=DEPTH)
        start = symbol
    line_match = re.match(r"^(\d+)A$", line)
    if line_match is None:
        raise NotImplementedError
    print(f"line = {line} result = {result} line_match = {line_match.group(1)}")
    return result * int(line_match.group(1))


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(line.strip())
    print(result)


if __name__ == "__main__":
    main()
