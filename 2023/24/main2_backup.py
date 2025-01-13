from __future__ import annotations
from typing import cast
import re
from sympy import symbols, Eq, solve

FILENAME = "demo.txt"  # expected 47
# FILENAME = "input.txt"

Line = tuple[int, int, int, int, int, int]


# def f(line1: Line, line2: Line) -> bool:
#     # line1: x = x1+a1*t, y=y1+b1*t, z=z1+b1*t
#     # line2: x = x2+a2*t, y=y2+b2*t, z=z2+b2*t
#     x1, y1, a1, b1 = line1[0], line1[1], line1[3], line1[4]
#     x2, y2, a2, b2 = line2[0], line2[1], line2[3], line2[4]
#     determinant = a1 * b2 - a2 * b1
#     if determinant == 0:
#         # print("parallel")
#         return False
#     t = (b2 * (x2 - x1) - a2 * (y2 - y1)) / determinant
#     s = (b1 * (x2 - x1) - a1 * (y2 - y1)) / determinant
#     if t < 0 or s < 0:
#         # print("crossed in the past")
#         return False
#     x = x1 + a1 * t
#     y = y1 + b1 * t

#     # print(f"cross at x = {x} y = {y} repeat ({x2+a2*s}, {y2+a2*s})")
#     return True
def f(lines):
    if len(lines) < 3:
        raise NotImplementedError
    x1=lines[0][0]
    x2=lines[1][0]
    x3=lines[2][0]
    y1=lines[0][1]
    y2=lines[1][1]
    y3=lines[2][1]
    z1=lines[0][2]
    z2=lines[2][2]
    z3=lines[3][2]
    a1=lines[0][3]
    a2=lines[1][3]
    a3=lines[2][3]
    b1=lines[0][4]
    b2=lines[1][4]
    b3=lines[2][4]
    c1=lines[0][5]
    c2=lines[2][5]
    c3=lines[3][5]




def main() -> None:
    lines = []
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = re.match(
                r"^(-?\d+),\s+(-?\d+),\s+(-?\d+)\s+@\s+(-?\d+),\s+(-?\d+),\s+(-?\d+)$",
                line_.strip(),
            )
            if line is None:
                raise NotImplementedError
            lines.append(cast(Line, tuple(map(int, line.groups()))))
    print(lines)
    # result = 0
    # for i in range(len(lines) - 1):
    #     print(f"i = {i}/{len(lines)}")
    #     for j in range(i + 1, len(lines)):
    #         # print(f"i = {i} {lines[i]} and j = {j} {lines[j]}")
    #         if f(lines[i], lines[j]):
    #             result += 1
    # print(result)
    print(f(lines))


if __name__ == "__main__":
    main()
