FILENAME = "demo2.txt"  # expected 6 0 4 12 4
FILENAME = "input.txt"


def f(line: str) -> int:
    result = 0
    for index in range(len(line)):
        if line[index] == line[(index + len(line) // 2) % len(line)]:
            result += int(line[index])
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
