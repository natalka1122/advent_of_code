FILENAME = "demo1.txt"  # expected 18
FILENAME = "input.txt"


def f(line: list[int]) -> int:
    return max(line) - min(line)


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(list(map(int, line.strip().replace("\t", " ").split(" "))))
    print(result)


if __name__ == "__main__":
    main()
