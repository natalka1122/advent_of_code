from __future__ import annotations
import re

# FILENAME = "demo.txt"  # expected 480
FILENAME = "input.txt"


def main():
    result = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if not line:
                continue
            a_match = re.match(r"Button A: X\+(\d+), Y\+(\d+)", line)
            if a_match is not None:
                x1 = int(a_match.group(1))
                y1 = int(a_match.group(2))
                continue
            b_match = re.match(r"Button B: X\+(\d+), Y\+(\d+)", line)
            if b_match is not None:
                x2 = int(b_match.group(1))
                y2 = int(b_match.group(2))
                continue
            prize_match = re.match(r"Prize: X=(\d+), Y=(\d+)", line)
            if prize_match is None:
                raise NotImplementedError
            x0 = int(prize_match.group(1))
            y0 = int(prize_match.group(2))
            print(x1, y1, x2, y2, x0, y0)
            b = (y0 * x1 - x0 * y1) // (y2 * x1 - x2 * y1)
            a = (x0 - b * x2) // x1
            print(f"a = {a} b = {b}")
            if a * x1 + b * x2 == x0 and a * y1 + b * y2 == y0:
                result += 3 * a + b
                print(f"good")
    print(result)


if __name__ == "__main__":
    main()
