FILENAME = "demo2.txt"  # expected 0 17 3 2 0 0 10
FILENAME = "input.txt"

OPEN_GARBAGE = "<"
CLOSE_GARBAGE = ">"
OPEN_GROUP = "{"
CLOSE_GROUP = "}"
MISS_NEXT = "!"


def f(line: str) -> int:
    stack = 0
    result = 0
    is_garbage = False
    miss_next = False
    for symbol in line:
        if is_garbage:
            if miss_next:
                miss_next = False
            elif symbol == CLOSE_GARBAGE:
                is_garbage = False
            elif symbol == MISS_NEXT:
                miss_next = True
            else:
                result += 1
        elif symbol == OPEN_GARBAGE:
            is_garbage = True
        elif symbol == OPEN_GROUP:
            stack += 1
        elif symbol == CLOSE_GROUP:
            stack -= 1
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
