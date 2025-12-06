# FILENAME = "demo.txt"  # expected 4277556
FILENAME = "input.txt"


def calc(line: list[str]) -> int:
    if line[-1] == "+":
        result = sum(map(int, line[:-1]))
    elif line[-1] == "*":
        result = 1
        for n in line[:-1]:
            result *= int(n)
    else:
        raise NotImplementedError
    return result


def main() -> None:
    lines: list[list[str]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            lines.append(list(filter(lambda x: len(x) > 0, line.strip().split(" "))))
    height = len(lines)
    width = len(lines[0])
    result = 0
    for j in range(width):
        column: list[str] = []
        for i in range(height):
            column.append(lines[i][j])
        result += calc(column)

    print(result)


if __name__ == "__main__":
    main()
