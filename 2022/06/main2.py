FILENAME = "demo.txt"  # expected 19, 23, 23, 29, 26
# FILENAME = "input.txt"
FOUR = 14


def f(line: str) -> int:
    for i in range(FOUR, len(line)):
        if len(set(line[i - FOUR : i])) == FOUR:
            return i
    raise NotImplementedError


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()