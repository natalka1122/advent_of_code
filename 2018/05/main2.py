FILENAME = "demo2.txt"  # expected 4
FILENAME = "input.txt"


def f(line: str) -> int:
    is_changed = True
    while is_changed:
        is_changed = False
        i = 0
        while i < len(line) - 1:
            if line[i].islower() and line[i + 1].isupper() and line[i] == line[i + 1].lower():
                line = line[:i] + line[i + 2 :]
                is_changed = True
            elif line[i].isupper() and line[i + 1].islower() and line[i].lower() == line[i + 1]:
                line = line[:i] + line[i + 2 :]
                is_changed = True
            i += 1
    return len(line)


def g(line: str) -> int:
    best_result = len(line)
    for letter in set(line.lower()):
        current_line = line.replace(letter, "").replace(letter.upper(), "")
        best_result = min(best_result, f(current_line))
    return best_result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(g(line.strip()))


if __name__ == "__main__":
    main()
