from collections import defaultdict
from typing import DefaultDict

# FILENAME = "demo.txt"  # expected 40
FILENAME = "input.txt"

START = "S"
SPLITTER = "^"


def main() -> None:
    field: list[str] = []
    with open(FILENAME, "r") as file:
        for line in file:
            field.append(line.rstrip("\n"))
    beams: DefaultDict[int, int] = defaultdict(int)
    beams[field[0].index(START)] = 1
    for line in field[1:]:
        new_beams: DefaultDict[int, int] = defaultdict(int)
        for index, count in beams.items():
            if line[index] == SPLITTER:
                new_beams[index - 1] += beams[index]
                new_beams[index + 1] += beams[index]
            else:
                new_beams[index] += count
        beams = new_beams
    print(sum(beams.values()))


if __name__ == "__main__":
    main()
