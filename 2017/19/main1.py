FILENAME = "demo.txt"  # expected ABCDEF
FILENAME = "input.txt"

NEW_LINE = "\n"
VERTICAL = "|"
HORIZONTAL = "-"
TURN = "+"
EMTPY = " "
DOWN = 1, 0
UP = -1, 0
LEFT = 0, -1
RIGHT = 0, 1


def main() -> None:
    diagram: list[str] = []
    with open(FILENAME, "r") as file:
        for line in file:
            if line[-1] == NEW_LINE:
                diagram.append((line[:-1]))
            else:
                diagram.append((line))
    print(diagram)
    result = ""
    y, x = 0, diagram[0].index(VERTICAL)
    dy, dx = 1, 0
    while True:
        if diagram[y][x].isupper():
            result += diagram[y][x]
        elif dx == 0:
            if diagram[y][x] == VERTICAL or diagram[y][x] == HORIZONTAL:
                pass
            elif diagram[y][x] == TURN:
                if diagram[y][x - 1] == EMTPY and diagram[y][x + 1] != EMTPY:
                    dy = 0
                    dx = 1
                elif diagram[y][x + 1] == EMTPY and diagram[y][x - 1] != EMTPY:
                    dy = 0
                    dx = -1
                else:
                    break
            else:
                break
        elif dy == 0:
            if diagram[y][x] == HORIZONTAL or diagram[y][x] == VERTICAL:
                pass
            elif diagram[y][x] == TURN:
                if y == 0 and diagram[y + 1][x] != EMTPY:
                    dy = 1
                    dx = 0
                elif y == len(diagram) - 1 and diagram[y - 1][x] != EMTPY:
                    dy = -1
                    dx = 0
                elif diagram[y - 1][x] == EMTPY and diagram[y + 1][x] != EMTPY:
                    dy = 1
                    dx = 0
                elif diagram[y + 1][x] == EMTPY and diagram[y - 1][x] != EMTPY:
                    dy = -1
                    dx = 0
                else:
                    break
            else:
                break
        else:
            break
        y += dy
        x += dx
        print((y, x), (dy, dx), diagram[y][x])
    print(result)


if __name__ == "__main__":
    main()
