# FILENAME = "demo.txt"
FILENAME = "input.txt"


def main() -> None:
    result = 0
    dial = 50
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            is_left = line[0] == "L"
            count = int(line[1:])
            for _ in range(count):
                if is_left:
                    dial -= 1
                    if dial == -1:
                        dial = 99
                else:
                    dial += 1
                    if dial == 100:
                        dial = 0
                if dial == 0:
                    result += 1
            print(f"{line}: {is_left}, {count} => {dial} result = {result}")
    print(result)


if __name__ == "__main__":
    main()
