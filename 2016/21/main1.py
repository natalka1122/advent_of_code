FILENAME, START = "demo.txt", "abcde"  # expected decab
FILENAME, START = "input.txt", "abcdefgh"

SWAP = "swap"
ROTATE = "rotate"
REVERSE = "reverse"
MOVE = "move"
POSITION = "position"
LETTER = "letter"
LEFT = "left"
RIGHT = "right"
BASED = "based"


def swap_position(x: int, y: int, line: str) -> str:
    if x < y:
        p1, p2 = x, y
    elif x > y:
        p1, p2 = y, x
    else:
        raise NotImplementedError
    return line[:p1] + line[p2] + line[p1 + 1 : p2] + line[p1] + line[p2 + 1 :]


def swap_letter(x: str, y: str, line: str) -> str:
    if line.count(x) != 1:
        raise NotImplementedError
    if line.count(y) != 1:
        raise NotImplementedError
    p1 = line.index(x)
    p2 = line.index(y)
    return swap_position(p1, p2, line)


def rotate_left(x: int, line: str) -> str:
    x = x % len(line)
    return line[x:] + line[:x]


def rotate_right(x: int, line: str) -> str:
    return rotate_left(-x, line)


def rotate_based(x: str, line: str) -> str:
    if line.count(x) != 1:
        raise NotImplementedError
    index = line.index(x)
    if index < 4:
        shift = index + 1
    else:
        shift = index + 2
    return rotate_right(shift, line)


def reverse(x: int, y: int, line: str) -> str:
    if x < y:
        p1, p2 = x, y
    elif x > y:
        p1, p2 = y, x
    else:
        raise NotImplementedError
    return line[:p1] + line[p1 : p2 + 1][::-1] + line[p2 + 1 :]


def move(x: int, y: int, line: str) -> str:
    if x < y:
        return line[:x] + line[x + 1 : y + 1] + line[x] + line[y + 1 :]
    if x > y:
        return line[:y] + line[x] + line[y:x] + line[x + 1 :]
    raise NotImplementedError


def main() -> None:
    result = START
    print(f"result = {result}")
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(" ")
            if line[0] == SWAP:
                if line[1] == POSITION and line[4] == POSITION:
                    result = swap_position(int(line[2]), int(line[5]), result)
                elif line[1] == LETTER and line[4] == LETTER:
                    result = swap_letter(line[2], line[5], result)
                else:
                    print(f"line = {line}")
                    raise NotImplementedError
            elif line[0] == ROTATE:
                if line[1] == LEFT:
                    result = rotate_left(int(line[2]), result)
                elif line[1] == RIGHT:
                    result = rotate_right(int(line[2]), result)
                elif line[1] == BASED:
                    result = rotate_based(line[6], result)
                else:
                    raise NotImplementedError
            elif line[0] == REVERSE:
                result = reverse(int(line[2]), int(line[4]), result)
            elif line[0] == MOVE:
                result = move(int(line[2]), int(line[5]), result)
            else:
                print(f"line = {line}")
                raise NotImplementedError
            print(f"line = {line}")
            print(f"result = {result}")


if __name__ == "__main__":
    main()
