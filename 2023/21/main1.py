from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"
# MAX_STEPS = 6
MAX_STEPS = 64
START = "S"
ROCK = "#"
EMPTY = "."


def main():
    the_map = []
    y = 0
    start = None
    with open(FILENAME, "r") as file:
        for line in file:
            the_map.append(line.strip())
            if START in the_map[-1]:
                if start is not None:
                    raise NotImplementedError
                start = y, the_map[-1].index(START)
            y += 1
    if start is None:
        raise NotImplementedError
    print(the_map)
    print(start)
    Q = {start}
    for step in range(MAX_STEPS):
        new_Q = set()
        for y, x in Q:
            for dy, dx in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if 0 <= y + dy < len(the_map) and 0 <= x + dx < len(the_map[0]):
                    if the_map[y + dy][x + dx] != ROCK:
                        new_Q.add((y + dy, x + dx))
        Q = new_Q
    print(len(new_Q))


if __name__ == "__main__":
    main()
