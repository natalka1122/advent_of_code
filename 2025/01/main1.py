# FILENAME = "demo.txt"
FILENAME = "input.txt"


def main() -> None:
    result = 0
    dial = 50
    with open(FILENAME, "r") as file:
        for line in file:
            is_left = line[0] == "L"
            count = int(line.strip()[1:])
            if is_left:
                count = -count
            dial = (dial + count) % 100
            if dial == 0:
                result += 1
            print(f"{is_left}, {count} => {dial}")
    print(result)


if __name__ == "__main__":
    main()
