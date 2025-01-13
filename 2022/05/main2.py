import re

FILENAME = "demo.txt"  # expected MCD
FILENAME = "input.txt"


def main() -> None:
    crates: list[list[str]] = []
    is_rearrangement = False
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                if is_rearrangement:
                    raise NotImplementedError
                is_rearrangement = True
                for i in range(len(crates)):
                    crates[i] = crates[i][::-1]
                # print(crates)
            elif is_rearrangement:
                line_match = re.match(r"move (\d+) from (\d+) to (\d+)", line.strip())
                if line_match is None:
                    raise NotImplementedError
                count = int(line_match.group(1))
                source = int(line_match.group(2)) - 1
                target = int(line_match.group(3)) - 1
                for i in range(count, 0, -1):
                    crates[target].append(crates[source][-i])
                for i in range(count):
                    crates[source].pop()
                # print(crates)
            else:
                if "[" in line:
                    for i in range((len(line)) // 4):
                        symbol = line[i * 4 + 1]
                        if len(crates) == i:
                            crates.append([])
                        if symbol != " ":
                            crates[i].append(symbol)
                else:
                    continue
    if not is_rearrangement:
        raise NotImplementedError
    print("".join(map(lambda x: x[-1], crates)))


if __name__ == "__main__":
    main()
