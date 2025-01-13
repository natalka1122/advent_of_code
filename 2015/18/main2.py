from __future__ import annotations

# FILENAME, STEPS = "demo2.txt", 5  # expected 17
FILENAME, STEPS = "input.txt", 100
ON = "#"
OFF = "."


def f(grid: list[list[str]]) -> list[list[str]]:
    result: list[list[str]] = []
    for y in range(len(grid)):
        result.append([])
        for x in range(len(grid[0])):
            neigbours = {
                (y - 1, x - 1),
                (y - 1, x),
                (y - 1, x + 1),
                (y, x - 1),
                (y, x + 1),
                (y + 1, x - 1),
                (y + 1, x),
                (y + 1, x + 1),
            }
            count_lights = 0
            for neigbour in filter(
                lambda k: 0 <= k[0] < len(grid) and 0 <= k[1] < len(grid[0]),
                neigbours,
            ):
                if grid[neigbour[0]][neigbour[1]] == ON:
                    count_lights += 1
            if grid[y][x] == ON:
                if count_lights in [2, 3]:
                    result[-1].append(ON)
                else:
                    result[-1].append(OFF)
            elif grid[y][x] == OFF:
                if count_lights == 3:
                    result[-1].append(ON)
                else:
                    result[-1].append(OFF)
    result[0][0] = ON
    result[0][-1] = ON
    result[-1][0] = ON
    result[-1][-1] = ON
    return result


def main() -> None:
    grid: list[list[str]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            grid.append(list(line.strip()))
    grid[0][0] = ON
    grid[0][-1] = ON
    grid[-1][0] = ON
    grid[-1][-1] = ON
    print(grid)
    for _ in range(STEPS):
        grid = f(grid)
        # for y in range(len(grid)):
        #     print("".join(grid[y]))
        # print("*")
    result = 0
    for y in range(len(grid)):
        result += grid[y].count(ON)
    print(result)


if __name__ == "__main__":
    main()
