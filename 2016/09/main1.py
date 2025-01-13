import re

FILENAME = "demo1.txt"
FILENAME = "input.txt"


def f(line: str) -> int:
    line_match = re.search(r"\((\d+)x(\d+)\)", line)
    if line_match is None:
        return len(line)
    result = line[: line_match.start(0)] + line[
        line_match.end(0) : line_match.end(0) + int(line_match.group(1))
    ] * int(line_match.group(2))
    return len(result) + f(line[line_match.end(0) + int(line_match.group(1)) :])


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
