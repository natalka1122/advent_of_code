# FILENAME = "demo.txt"
FILENAME = "input.txt"
FOURTY = 50


def f(line: str) -> str:
    result = ""
    index = 0
    while index < len(line):
        j = index + 1
        while j < len(line) and line[j] == line[index]:
            j += 1
        result += str(j - index) + line[index]
        index = j
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            x = line.strip()
            for i in range(FOURTY):
                x = f(x)
            print(len(x))


if __name__ == "__main__":
    main()
