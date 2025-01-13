import hashlib

FILENAME = "demo0.txt"  # expected not found
FILENAME = "demo1.txt"  # expected DDRRRD
FILENAME = "demo2.txt"  # expected DDUDRLRRUDRD
FILENAME = "demo3.txt"  # expected DRURDRUDDLLDLUURRDULRLDUUDDDRR
FILENAME = "input.txt"
START = 0, 0
TARGET = 3, 3
HEIGHT = 4
WIDTH = 4
D = "D"
U = "U"
L = "L"
R = "R"
DIRECTIONS = [(U, 0 - 1, 0), (D, 1, 0), (L, 0, -1), (R, 0, 1)]
ALLOWED = "bcdef"


def md5(line: str) -> str:
    return hashlib.md5(line.encode()).hexdigest()


def f(line: str) -> str:
    Q = [("", START)]
    while len(Q) > 0:
        path, current = Q.pop(0)
        y0, x0 = current
        current_hash = md5(line + path)
        # print(current_hash)
        for index, value in enumerate(DIRECTIONS):
            if current_hash[index] not in ALLOWED:
                continue
            letter, dy, dx = value
            y = y0 + dy
            x = x0 + dx
            if 0 <= y < HEIGHT and 0 <= x < WIDTH:
                if (y, x) == TARGET:
                    return path + letter
                Q.append((path + letter, (y, x)))

    return "not found"


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line))


if __name__ == "__main__":
    main()
