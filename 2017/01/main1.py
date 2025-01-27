FILENAME = "demo1.txt"  # expected 3 4 0 9
FILENAME = "input.txt"


def f(line: str) -> int:
    result = 0
    for index in range(len(line)):
        if line[index - 1] == line[index]:
            result += int(line[index])
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
