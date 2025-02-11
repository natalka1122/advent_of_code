FILENAME = "demo1.txt"  # expected 34241
FILENAME = "input.txt"


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += int(line) // 3 - 2
    print(result)


if __name__ == "__main__":
    main()
