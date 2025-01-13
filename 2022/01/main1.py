FILENAME = "demo.txt"  # expected 24000
FILENAME = "input.txt"


def main() -> None:
    result = 0
    current_elf = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                result = max(result, current_elf)
                current_elf = 0
            else:
                current_elf += int(line)
    result = max(result, current_elf)
    print(result)


if __name__ == "__main__":
    main()
