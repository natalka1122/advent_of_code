FILENAME = "demo.txt"  # expected 45000
FILENAME = "input.txt"
THREE = 3


def main() -> None:
    result = [0, 0, 0]
    current_elf = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                result.append(current_elf)
                result = sorted(result, reverse=True)[:THREE]

                current_elf = 0
            else:
                current_elf += int(line)
    result.append(current_elf)
    result = sorted(result, reverse=True)[:THREE]
    print(sum(result))


if __name__ == "__main__":
    main()
