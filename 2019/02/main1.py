FILENAME = "input.txt"


def f(program: list[int]) -> int:
    print(program)
    program[1] = 12
    program[2] = 2
    i = 0
    while program[i] != 99:
        if program[i] == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
        elif program[i] == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
        i = i + 4
        print(program)
    return program[0]


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(list(map(int, line.split(",")))))


if __name__ == "__main__":
    main()
