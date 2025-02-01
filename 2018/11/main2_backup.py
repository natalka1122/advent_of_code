FILENAME = "demo.txt"  # expected 3,45 21,61
# FILENAME = "input.txt"

GRID_SIZE = 300
# GRID_SIZE = 5
SMALL_NUMBER = -GRID_SIZE * GRID_SIZE * 10


def f(num: int) -> tuple[int, int]:
    grid: list[list[int]] = []
    for y in range(1, GRID_SIZE + 1):
        grid.append([])
        for x in range(1, GRID_SIZE + 1):
            grid[-1].append(((x + 10) * y + num) * (x + 10) // 100 % 10 - 5)
            # grid[-1].append(1)
    best_sum = SMALL_NUMBER
    best_coord = -1, -1
    for y0 in range(GRID_SIZE):
        for x0 in range(GRID_SIZE):
            # print(f"y0 = {y0}", f"x0 = {x0}")
            current_sum = 0
            for size in range(GRID_SIZE - max(y0, x0)):
                # print(f"size = {size}")
                # print(y0, x0, size, "=>", end="")
                # for y in range(y0, y0 + size):
                # for x in range(x0, x0 + size):
                y = y0 + size
                for x in range(x0 + size):
                    # print(f"y = {y}", f"x = {x}")
                    current_sum += grid[y][x]
                x = x0 + size
                for y in range(y0 + size):
                    # print(f"y = {y}", f"x = {x}")
                    current_sum += grid[y][x]
                # print(f"y = {y0 + size}", f"x = {x0 + size}")
                current_sum += grid[y0 + size][x0 + size]
                # print(f"current_sum = {current_sum}")
                if best_sum < current_sum:
                    best_sum = current_sum
                    best_coord = y0, x0, size
                    print(f"best_sum = {best_sum}", f"best_coord = {best_coord}")

    # if True:
    #         current_sum = 0
    #         for y in range(y0, y0 + THREE):
    #             for x in range(x0, x0 + THREE):
    #                 current_sum += grid[y][x]
    #         if current_sum > best_sum:
    #             best_sum = current_sum
    #             best_coord = x0, y0
    return best_coord[0] + 1, best_coord[1] + 1, best_coord[2] + 2
    return -1, -1


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(",".join(map(str, f(int(line)))))


if __name__ == "__main__":
    main()
