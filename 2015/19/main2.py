FILENAME = "demo2_1.txt"  # expected 3
FILENAME = "demo2_2.txt"  # expected 6
FILENAME = "input.txt"
E = "e"

def f(line: str, replacements: dict[str, set[str]]) -> str:
    result = None
    for index in range(len(line)):
        for source, targets in replacements.items():
            if line[index:].startswith(source):
                for target in targets:
                    current = line[:index] + target + line[index + len(source) :]
                    if result is None or len(current) < len(result):
                        result = current
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
                if b not in replacements:
                    replacements[b] = set()
                replacements[b].add(a)
    if start_line is None:
        raise NotImplementedError
    print(replacements)
    line = start_line
    step = 0
    while len(line)> 1:
        step += 1
        line = f(line, replacements)
        print(line)
    if line != E:
        step +=1
    print(step)


if __name__ == "__main__":
    main()
