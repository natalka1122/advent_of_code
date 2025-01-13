# from __future__ import annotations
from typing import Optional
import functools
import re

FILENAME = "demo.txt"  # expected 126384
FILENAME = "input.txt"
A = "A"
LEFT = "<"
RIGHT = ">"
UP = "^"
DOWN = "v"
DIGITS = "1234567890A"
DIRECTIONS = "^<>vA"


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


@functools.cache
def apply(num, d1, d2, button) -> Optional[tuple[str, str, str, Optional[str]]]:
    if button == A:
        if d2 == A:
            if d1 == A:
                return num, d1, d2, num
            num_state = do_numerical(num, d1)
            if num_state is not None:
                return num_state, d1, d2, None
            return None
        d1_state = do_directional(d1, d2)
        if d1_state is not None:
            return num, d1_state, d2, None
        return None
    d2_state = do_directional(d2, button)
    if d2_state is not None:
        return num, d1, d2_state, None
    return None


def calc(source: str, target: str) -> int:
    print(f"calc: source = {source} target = {target}")
    Q = {(0, source, A, A)}
    visited = set()
    while len(Q) > 0:
        min_elem = min(Q, key=lambda x: x[0])
        visited.add(min_elem)
        distance, num, d1, d2 = min_elem
        Q.remove(min_elem)
        for button in DIRECTIONS:
            button_apply = apply(num, d1, d2, button)
            if button_apply is None:
                continue
            if button_apply[3] is None:
                new_elem = (
                    distance + 1,
                    button_apply[0],
                    button_apply[1],
                    button_apply[2],
                )
                if new_elem not in visited:
                    Q.add(new_elem)
            elif button_apply[3] == target:
                return distance + 1
            else:
                continue
    raise NotImplementedError


def f(line: str) -> int:
    result = 0
    start = A
    for symbol in line:
        result += calc(start, symbol)
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
