FILENAME = "demo18.txt"  # expected 3,45
FILENAME = "demo42.txt"  # expected 21,61
FILENAME = "input.txt"

GRID_SIZE = 300
THREE = 3
SMALL_NUMBER = -100


def f(num: int) -> tuple[int, int]:
    grid: list[list[int]] = []
    for y in range(1, GRID_SIZE + 1):
        grid.append([])
        for x in range(1, GRID_SIZE + 1):
            grid[-1].append(((x + 10) * y + num) * (x + 10) // 100 % 10 - 5)
    best_sum = SMALL_NUMBER
    best_coord = -1, -1
    for y0 in range(GRID_SIZE - THREE):
        for x0 in range(GRID_SIZE - THREE):
            current_sum = 0
            for y in range(y0, y0 + THREE):
                for x in range(x0, x0 + THREE):
                    current_sum += grid[y][x]
            if current_sum > best_sum:
                best_sum = current_sum
                best_coord = x0, y0
    return best_coord[0] + 1, best_coord[1] + 1


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(",".join(map(str, f(int(line)))))


if __name__ == "__main__":
    main()
