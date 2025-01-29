FILENAME, ITERATION_COUNT = "demo.txt", 2  # expected 12
FILENAME, ITERATION_COUNT = "input.txt", 5

START = [".#.", "..#", "###"]
DIV = "/"
GRID = "#"
FOUR = 4
TWO = 2
THREE = 3


def sq_to_line(sq: list[str]) -> str:
    return DIV.join(sq)


def line_to_sq(line: str) -> list[str]:
    return line.split(DIV)


def flip(line: str) -> str:
    sq = line_to_sq(line)
    result: list[str] = []
    size = len(sq)
    if size != len(sq[0]):
        raise NotImplementedError
    for y in range(size):
        result.append("")
        for x in range(size):
            result[-1] += sq[y][size - x - 1]
    return sq_to_line(result)


def rotate(line: str) -> str:
    sq = line_to_sq(line)
    result: list[str] = []
    size = len(sq)
    if size != len(sq[0]):
        raise NotImplementedError
    for x in range(size):
        result.append("")
        for y in range(size):
            result[-1] += sq[y][x]
    return sq_to_line(result)


def main() -> None:
    enhancement_rules: dict[str, str] = {}
    with open(FILENAME, "r") as file:
        for line_ in file:
            source_pattern, destination_pattern = line_.strip().split(" => ")
            for i in range(FOUR):
                if source_pattern in enhancement_rules:
                    if enhancement_rules[source_pattern] != destination_pattern:
                        raise NotImplementedError
                else:
                    enhancement_rules[source_pattern] = destination_pattern
                source_pattern = flip(source_pattern)
                if source_pattern in enhancement_rules:
                    if enhancement_rules[source_pattern] != destination_pattern:
                        raise NotImplementedError
                else:
                    enhancement_rules[source_pattern] = destination_pattern
                if i < FOUR - 1:
                    source_pattern = rotate(source_pattern)
                    if source_pattern in enhancement_rules:
                        if enhancement_rules[source_pattern] != destination_pattern:
                            raise NotImplementedError
                    else:
                        enhancement_rules[source_pattern] = destination_pattern
    # print(enhancement_rules)
    pattern = START
    for _ in range(ITERATION_COUNT):
        size = len(pattern)
        result = []
        if size % TWO == 0:
            for y0 in range(size // TWO):
                for dy in range(TWO + 1):
                    result.append("")
                for x0 in range(size // TWO):
                    source = []
                    for dy in range(TWO):
                        source.append("")
                        for dx in range(TWO):
                            source[-1] += pattern[y0 * TWO + dy][x0 * TWO + dx]
                    destination = line_to_sq(enhancement_rules[sq_to_line(source)])
                    for dy in range(TWO + 1):
                        result[y0 * (TWO + 1) + dy] += destination[dy]
        elif size % THREE == 0:
            for y0 in range(size // THREE):
                for dy in range(THREE + 1):
                    result.append("")
                for x0 in range(size // THREE):
                    source = []
                    for dy in range(THREE):
                        source.append("")
                        for dx in range(THREE):
                            source[-1] += pattern[y0 * THREE + dy][x0 * THREE + dx]
                    destination = line_to_sq(enhancement_rules[sq_to_line(source)])
                    for dy in range(THREE + 1):
                        result[y0 * (THREE + 1) + dy] += destination[dy]
        else:
            raise NotImplementedError
        pattern = result
    print(sq_to_line(pattern).count(GRID))


if __name__ == "__main__":
    main()
