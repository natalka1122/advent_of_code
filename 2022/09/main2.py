FILENAME = "demo.txt"  # expected 1
FILENAME = "demo2.txt"  # expected 36
FILENAME = "input.txt"


Point = tuple[int, int]
DIRECTIONS = {"L": (0, -1), "R": (0, 1), "U": (1, 0), "D": (-1, 0)}
TAIL = 10


def sign(a: int, b: int) -> int:
    if a < b:
        return -1
    if a > b:
        return 1
    if a == b:
        return 0
    raise NotImplementedError


def f(H: Point, T: Point) -> Point:
    if abs(H[0] - T[0]) >= 3 or abs(H[1] - T[1]) >= 3:
        raise NotImplementedError
    if abs(H[0] - T[0]) <= 1 and abs(H[1] - T[1]) <= 1:
        return T
    if H[0] == T[0]:
        if abs(T[1] - H[1]) == 2:
            return T[0], T[1] + sign(H[1], T[1])
        else:
            raise NotImplementedError
    if H[1] == T[1]:
        if abs(T[0] - H[0]) == 2:
            return T[0] + sign(H[0], T[0]), T[1]
        else:
            raise NotImplementedError
    if abs(T[0] - H[0]) + abs(T[1] - H[1]) == 3:
        return T[0] + sign(H[0], T[0]), T[1] + sign(H[1], T[1])
    if abs(T[0] - H[0]) + abs(T[1] - H[1]) == 4:
        return T[0] + sign(H[0], T[0]), T[1] + sign(H[1], T[1])
    print(f"H = {H} T = {T}")
    raise NotImplementedError


def main() -> None:
    visited: set[Point] = set()
    rope = []
    for _ in range(TAIL):
        rope.append((0, 0))
    with open(FILENAME, "r") as file:
        for line in file:
            direction = DIRECTIONS[line.strip().split(" ")[0]]
            count = int(line.strip().split(" ")[1])
            for i in range(count):
                # print(rope[0],"=>",end=" ")
                rope[0] = rope[0][0] + direction[0], rope[0][1] + direction[1]
                # print(rope[0])
                for j in range(1, TAIL):
                    # print(rope[j],"=>",end=" ")
                    rope[j] = f(rope[j - 1], rope[j])
                    # print(rope[j])
                visited.add(rope[-1])
                # print(f"{line.strip().split(' ')[0]} {i+1} {rope}")
    print(len(visited))


if __name__ == "__main__":
    main()
