FILENAME = "demo.txt"  # expected 820
FILENAME = "input.txt"


def f(line: str) -> int:
    a = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    b = int(line[7:].replace("L", "0").replace("R", "1"), 2)
    return 8 * a + b


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result = max(result, f(line.strip()))
    print(result)


if __name__ == "__main__":
    main()
