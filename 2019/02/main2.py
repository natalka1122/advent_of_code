FILENAME = "input.txt"

TARGET = 19690720


def f(program: list[int]) -> int:
    # print(program)
    # program[1] = 12
    # program[2] = 2
    i = 0
    while program[i] != 99:
        if program[i] == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
        elif program[i] == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
        i = i + 4
    print("program[0]",program[0])
    return program[0]


def calc(program: list[int]) -> int:
    for i in range(10000):
        for j in range(10000):
            try:
                if f([program[0], i, j] + program[2:]) == TARGET:
                    print("gotcha", i, j)
                    break
            except IndexError:
                continue
        print(f"i = {i}")


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(calc(list(map(int, line.split(",")))))


if __name__ == "__main__":
    main()
