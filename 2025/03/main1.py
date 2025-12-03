# FILENAME = "demo.txt"
FILENAME = "input.txt"


def f(line: list[int]) -> int:
    for first in range(9, 0, -1):
        try:
            first_index = line.index(first)
        except ValueError:
            continue
        for second in range(9, 0, -1):
            if second in line[first_index + 1 :]:
                return 10 * first + second
    return 0


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(list(map(int, line.strip())))
    print(result)


if __name__ == "__main__":
    main()
