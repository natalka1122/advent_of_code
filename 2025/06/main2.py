# FILENAME = "demo.txt"  # expected 3263827
FILENAME = "input.txt"


def calc(line: list[str]) -> int:
    operator = line[0][-1]
    numbers: list[int] = []
    for num_str in line:
        try:
            num = int(num_str)
        except ValueError:
            num = int(num_str[:-1])
        numbers.append(num)
    if operator == "+":
        result = sum(map(int, numbers))
    elif operator == "*":
        result = 1
        for n in numbers:
            result *= int(n)
    else:
        raise NotImplementedError
    return result


def main() -> None:
    field: list[str] = []
    with open(FILENAME, "r") as file:
        for line in file:
            field.append(line.rstrip("\n"))
    height = len(field)
    width = len(field[0])
    result = 0
    problem: list[str] = []
    for x in range(width):
        column = ""
        for y in range(height):
            column += field[y][x]
        if len(column.strip()) == 0:
            result += calc(problem)
            problem = []
        else:
            problem.append(column)
    result += calc(problem)
    print(result)


if __name__ == "__main__":
    main()
