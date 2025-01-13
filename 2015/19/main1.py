# FILENAME = "demo1_1.txt"  # expected 4
# FILENAME = "demo1_2.txt"  # expected 7
FILENAME = "input.txt"


def f(line: str, replacements: dict[str, set[str]]) -> set[str]:
    result = set()
    for index in range(len(line)):
        for source, targets in replacements.items():
            if line[index:].startswith(source):
                for target in targets:
                    result.add(line[:index] + target + line[index + len(source) :])
    print(result)
    return result


def main() -> None:
    replacements: dict[str, set[str]] = dict()
    final_line = False
    start_line = None
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                if final_line:
                    raise NotImplementedError
                final_line = True
            elif final_line:
                start_line = line
            else:
                a, b = line.split(" => ")
                if a not in replacements:
                    replacements[a] = set()
                replacements[a].add(b)
    if start_line is None:
        raise NotImplementedError
    print(replacements)
    print(len(f(start_line, replacements)))


if __name__ == "__main__":
    main()
