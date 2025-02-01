FILENAME = "demo18.txt"  # expected 90,269,16
FILENAME = "demo42.txt"  # expected 232,251,12
FILENAME = "input.txt"

GRID_SIZE = 300
SMALL_NUMBER = -GRID_SIZE * GRID_SIZE * 10


def f(num: int) -> tuple[int, int, int]:
    grid: list[list[int]] = [[0 for _ in range(GRID_SIZE + 1)]]
    I: list[list[int]] = [[0 for _ in range(GRID_SIZE + 1)]]
    best_sum: int = SMALL_NUMBER
    best_coord: tuple[int, int, int] = -1, -1, -1
    for x in range(1, GRID_SIZE + 1):
        grid.append([0])
        I.append([0])
        for y in range(1, GRID_SIZE + 1):
            grid[x].append(((x + 10) * y + num) * (x + 10) // 100 % 10 - 5)
            I[x].append(grid[x][y] + I[x - 1][y] + I[x][y - 1] - I[x - 1][y - 1])
            if y == x and best_sum < I[x][y]:
                best_sum = I[x][y]
                best_coord = 1, 1, x
    for x in range(1, GRID_SIZE + 1):
        for y in range(1, GRID_SIZE + 1):
            for size in range(1, GRID_SIZE - max(y, x)):
                if x + size - 1 > GRID_SIZE or y + size - 1 > GRID_SIZE:
                    break
                current_sum = (
                    I[x + size - 1][y + size - 1]
                    - I[x - 1][y + size - 1]
                    - I[x + size - 1][y - 1]
                    + I[x - 1][y - 1]
                )
                if best_sum < current_sum:
                    best_sum = current_sum
                    best_coord = x, y, size
    print(f"best_sum = {best_sum}")
    return best_coord


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(",".join(map(str, f(int(line)))))


if __name__ == "__main__":
    main()
