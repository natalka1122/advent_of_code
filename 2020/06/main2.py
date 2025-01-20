FILENAME = "demo.txt"  # expected 6
FILENAME = "demo1.txt"  # expected 3
FILENAME = "input.txt"


def main() -> None:
    result = 0
    groups: set[str] = set()
    is_first_line = True
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                result += len(groups)
                groups = set()
                is_first_line = True
            elif is_first_line:
                groups = set(line)
                is_first_line = False
            else:
                exclude = set()
                for letter in groups:
                    if letter not in line:
                        exclude.add(letter)
                for letter in exclude:
                    groups.remove(letter)
            # print(line)
    result += len(groups)
    print(result)


if __name__ == "__main__":
    main()
