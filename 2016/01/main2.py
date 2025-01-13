# FILENAME = "demo4.txt"  # expected 4
FILENAME = "input.txt"

DIRECTION = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def rotate(dy: int, dx: int, direction: str) -> tuple[int, int]:
    index = DIRECTION.index((dy, dx))
    if direction == "R":
        index += 1
    elif direction == "L":
        index -= 1
    else:
        raise NotImplementedError
    if index == len(DIRECTION):
        index = 0
    elif index == -1:
        index == len(DIRECTION) - 1
    return DIRECTION[index]


def f(the_list: list[str]) -> int:
    y0, x0 = 0, 0
    y, x = y0, x0
    dy, dx = 0, 1
    visited = {(0, 0)}
    found = False
    for direction in the_list:
        dy, dx = rotate(dy, dx, direction[0])
        for _ in range(int(direction[1:])):
            y += dy
            x += dx
            if (y, x) in visited:
                found = True
                break
            visited.add((y, x))
        if found:
            break
    return abs(y) + abs(x)


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(list(line.strip().split(", "))))


if __name__ == "__main__":
    main()
