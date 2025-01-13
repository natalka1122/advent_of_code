from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"
UNKNOWN = "."
OUTSIDE = "o"
INSIDE = "i"
BORDER = "B"


def main():
    current = (0, 0)
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    dig_plan = {current}
    with open(FILENAME, "r") as file:
        for line in file:
            direction_str, length_str, _ = line.split(" ")
            length = int(length_str)
            if direction_str == "L":
                direction = (0, -1)
            elif direction_str == "R":
                direction = (0, 1)
            elif direction_str == "U":
                direction = (-1, 0)
            elif direction_str == "D":
                direction = (1, 0)
            else:
                raise NotImplementedError
            print(f"length = {length} direction = {direction}")
            for _ in range(length):
                current = current[0] + direction[0], current[1] + direction[1]
                min_y = min(min_y, current[0])
                max_y = max(max_y, current[0])
                min_x = min(min_x, current[1])
                max_x = max(max_x, current[1])
                print(current)
                dig_plan.add(current)
    print(f"{min_y} <= y <= {max_y} {min_x} <= x <= {max_x}")
    the_map: list[list[str]] = []
    for _ in range(min_y - 1, max_y + 2):
        the_map.append([])
        for _ in range(min_x - 1, max_x + 2):
            the_map[-1].append(UNKNOWN)
    for y, x in dig_plan:
        the_map[y - min_y + 1][x - min_x + 1] = BORDER
    for y in range(len(the_map)):
        print("".join(the_map[y]))
    outsides = set()
    Q = [(0, 0)]
    while len(Q) > 0:
        y, x = Q.pop()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= y + dy < len(the_map) and 0 <= x + dx < len(the_map[0]):
                if the_map[y + dy][x + dx] == UNKNOWN:
                    outsides.add((y + dy, x + dx))
                    Q.append((y + dy, x + dx))
                    the_map[y + dy][x + dx] = OUTSIDE
    for y in range(len(the_map)):
        print("".join(the_map[y]))
    print(len(the_map)*len(the_map[0])-len(outsides))


if __name__ == "__main__":
    main()
