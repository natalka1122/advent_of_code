# FILENAME = "demo.txt"  # expected 21
FILENAME = "input.txt"

START = "S"
SPLITTER = "^"


def main() -> None:
    field: list[str] = []
    with open(FILENAME, "r") as file:
        for line in file:
            field.append(line.rstrip("\n"))
    result = 0
    beams: set[int] = set([field[0].index(START)])
    for line in field[1:]:
        to_add: set[int] = set()
        to_delete: set[int] = set()
        for beam in beams:
            if line[beam] == SPLITTER:
                result += 1
                to_delete.add(beam)
                to_add.add(beam - 1)
                to_add.add(beam + 1)
        if to_delete & to_add:
            raise NotImplementedError
        for beam in to_delete:
            beams.remove(beam)
        for beam in to_add:
            beams.add(beam)

    print(result)


if __name__ == "__main__":
    main()
