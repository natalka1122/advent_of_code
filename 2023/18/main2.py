from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"
UNKNOWN = "."
OUTSIDE = "o"
INSIDE = "i"
BORDER = "B"


def main() -> None:
    current = (0, 0)
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    dig_plan = [current]
    all_y_set = {-1, 0, 1}
    all_x_set = {-1, 0, 1}
    with open(FILENAME, "r") as file:
        for line in file:
            _, _, hexadecimal = line.strip().split(" ")
            length = int(hexadecimal[2:-2], 16)
            direction_str = hexadecimal[-2]
            if direction_str == "2":
                direction = (0, -1)
            elif direction_str == "0":
                direction = (0, 1)
            elif direction_str == "3":
                direction = (-1, 0)
            elif direction_str == "1":
                direction = (1, 0)
            else:
                print(f"hexadecimal = {hexadecimal} direction_str = {direction_str}")
                raise NotImplementedError
            print(
                f"hexadecimal = {hexadecimal} length = {length} direction = {direction}"
            )
            current = (
                current[0] + length * direction[0],
                current[1] + length * direction[1],
            )
            min_y = min(min_y, current[0])
            max_y = max(max_y, current[0])
            min_x = min(min_x, current[1])
            max_x = max(max_x, current[1])
            dig_plan.append(current)
            all_y_set.add(current[0] - 1)
            all_y_set.add(current[0])
            all_y_set.add(current[0] + 1)
            all_x_set.add(current[1] - 1)
            all_x_set.add(current[1])
            all_x_set.add(current[1] + 1)
    print(f"{min_y} <= y <= {max_y} {min_x} <= x <= {max_x}")
    print(f"dig_plan = {dig_plan}")
    all_y = sorted(all_y_set)
    all_x = sorted(all_x_set)
    print(f"all_y = {sorted(all_y)}")
    print(f"all_x = {sorted(all_x)}")
    the_map: list[list[str]] = []
    for _ in range(len(all_y)):
        the_map.append([])
        for _ in range(len(all_x)):
            the_map[-1].append(UNKNOWN)
    for i in range(len(dig_plan) - 1):
        y1 = all_y.index(dig_plan[i][0])
        y2 = all_y.index(dig_plan[i + 1][0])
        x1 = all_x.index(dig_plan[i][1])
        x2 = all_x.index(dig_plan[i + 1][1])
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                the_map[y][x] = BORDER
    Q = [(0, 0)]
    while len(Q) > 0:
        y, x = Q.pop()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= y + dy < len(the_map) and 0 <= x + dx < len(the_map[0]):
                if the_map[y + dy][x + dx] == UNKNOWN:
                    Q.append((y + dy, x + dx))
                    the_map[y + dy][x + dx] = OUTSIDE
    for y in range(len(the_map)):
        print("".join(the_map[y]))

    result = 0
    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            # Correctness check
            # if the_map[y][x] == BORDER:
            #     print(
            #         f"y = {y} x = {x} all_y = {all_y[y - 1 : y + 2]}, all_x = {all_x[x - 1 : x + 2]}"
            #     )
            #     if (all_y[y] - all_y[y - 1] == 1 and all_y[y + 1] - all_y[y] == 1) or (
            #         all_x[x] - all_x[x - 1] == 1 and all_x[x + 1] - all_x[x] == 1
            #     ):
            #         print("TODO")
            #     else:
            #         raise NotImplementedError
            if the_map[y][x] in [UNKNOWN, BORDER]:
                dy = all_y[y + 1] - all_y[y]
                dx = all_x[x + 1] - all_x[x]
                result += dy*dx
            elif the_map[y][x]!=OUTSIDE:
                raise NotImplementedError
    print(result)
    return
    # the_map: list[list[str]] = []
    # for _ in range(min_y - 1, max_y + 2):
    #     the_map.append([])
    #     for _ in range(min_x - 1, max_x + 2):
    #         the_map[-1].append(UNKNOWN)
    # for y, x in dig_plan:
    #     the_map[y - min_y + 1][x - min_x + 1] = BORDER
    # for y in range(len(the_map)):
    #     print("".join(the_map[y]))
    # outsides = set()
    # Q = [(0, 0)]
    # while len(Q) > 0:
    #     y, x = Q.pop()
    #     for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    #         if 0 <= y + dy < len(the_map) and 0 <= x + dx < len(the_map[0]):
    #             if the_map[y + dy][x + dx] == UNKNOWN:
    #                 outsides.add((y + dy, x + dx))
    #                 Q.append((y + dy, x + dx))
    #                 the_map[y + dy][x + dx] = OUTSIDE
    # for y in range(len(the_map)):
    #     print("".join(the_map[y]))
    # print(len(the_map) * len(the_map[0]) - len(outsides))


if __name__ == "__main__":
    main()
