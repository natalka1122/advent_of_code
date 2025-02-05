FILENAME = "demo2.txt"  # expected 9 5 18 2018
FILENAME = "input.txt"

START_LINE = "37"
TEN = 5


def f(target: str) -> str:
    index1 = 0
    index2 = 1
    line = START_LINE
    i = 0
    while len(line) <= len(target) or line[-len(target) :] != target:
        line += str(int(line[index1]) + int(line[index2]))
        index1 = (index1 + int(line[index1]) + 1) % len(line)
        index2 = (index2 + int(line[index2]) + 1) % len(line)
        # print(line, line[-len(target) :], target, len(line)-len(target))
        i += 1
        if i % 100 == 0:
            print(i)
        if i > 509671:
            break
    return len(line)-len(target)


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
