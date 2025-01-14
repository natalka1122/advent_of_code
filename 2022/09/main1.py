FILENAME = "demo.txt"  # expected 13
FILENAME = "input.txt"


Point = tuple[int, int]
DIRECTIONS = {"L": (0, -1), "R": (0, 1), "U": (1, 0), "D": (-1, 0)}


def sign(a: int, b: int) -> int:
    if a < b:
        return -1
    if a > b:
        return 1
    if a == b:
        return 0
    raise NotImplementedError


def f(H: Point, T: Point, direction: Point) -> tuple[Point, Point]:
    H = H[0] + direction[0], H[1] + direction[1]
    if abs(H[0] - T[0]) >= 3 or abs(H[1] - T[1]) >= 3:
        raise NotImplementedError
    if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
        return H, T
    if H[0] == T[0]:
        if abs(T[1] - H[1]) == 2:
            T = T[0], T[1] + sign(H[1], T[1])
        else:
            raise NotImplementedError
    elif H[1] == T[1]:
        if abs(T[0] - H[0]) == 2:
            T = T[0] + sign(H[0], T[0]), T[1]
        else:
            raise NotImplementedError
    elif abs(T[0] - H[0]) + abs(T[1] - H[1]) == 3:
        T = T[0] + sign(H[0], T[0]), T[1] + sign(H[1], T[1])
    else:
        raise NotImplementedError
    return H, T


def main() -> None:
    visited: set[Point] = set()
    H = 0, 0
    T = 0, 0
    with open(FILENAME, "r") as file:
        for line in file:
            direction = DIRECTIONS[line.strip().split(" ")[0]]
            count = int(line.strip().split(" ")[1])
            for i in range(count):
                H, T = f(H, T, direction)
                visited.add(T)
    print(len(visited))


if __name__ == "__main__":
    main()
