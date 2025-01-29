FILENAME = "demo1.txt"  # expected 3
FILENAME = "input.txt"


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if line[0] == "+":
                result += int(line[1:])
            else:
                result += int(line)
    print(result)


if __name__ == "__main__":
    main()
