from __future__ import annotations
import re
from sympy import solve, symbols

FILENAME = "demo.txt"  # expected 47
FILENAME = "input.txt"

Line = tuple[int, int, int, int, int, int]


def main() -> None:
    lines: list[Line] = []
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"^(-?\d+),\s+(-?\d+),\s+(-?\d+)\s+@\s+(-?\d+),\s+(-?\d+),\s+(-?\d+)$",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            groups = tuple(map(int, line_match.groups()))
            if len(groups) != 6:
                raise NotImplementedError
            lines.append(groups)
    a0, b0, c0, d0, e0, f0, t1, t2, t3 = symbols("a0, b0, c0, d0 e0 f0 t1 t2 t3")
    variables = [a0, b0, c0, d0, e0, f0, t1, t2, t3]
    a1, c1, e1, b1, d1, f1 = lines[0]
    a2, c2, e2, b2, d2, f2 = lines[1]
    a3, c3, e3, b3, d3, f3 = lines[2]
    equations = [
        a1 * t1 + b1 - a0 * t1 - b0,
        a2 * t2 + b2 - a0 * t2 - b0,
        a3 * t3 + b3 - a0 * t3 - b0,
        c1 * t1 + d1 - c0 * t1 - d0,
        c2 * t2 + d2 - c0 * t2 - d0,
        c3 * t3 + d3 - c0 * t3 - d0,
        e1 * t1 + f1 - e0 * t1 - f0,
        e2 * t2 + f2 - e0 * t2 - f0,
        e3 * t3 + f3 - e0 * t3 - f0,
    ]
    result = solve(equations, variables, dict=True)
    print(result)
    if len(result) != 1:
        raise NotImplementedError
    current_result = result.pop()
    print(current_result[a0] + current_result[c0] + current_result[e0])


if __name__ == "__main__":
    main()
