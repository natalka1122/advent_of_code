import re

FILENAME = "input.txt"


def main() -> None:
    nodes = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.search(
                r"node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)\%", line
            )
            if line_match is None:
                print(f"skipped {line.strip()}")
            else:
                key = (line_match.group(1), line_match.group(2))
                if key in nodes:
                    raise NotImplementedError
                nodes[key] = tuple(map(int,line_match.groups()[2:]))
    print(nodes)
    result = 0
    for node1 in nodes:
        if nodes[node1][1] == 0:
            continue
        for node2 in nodes:
            if node1 == node2:
                continue
            if nodes[node1][1] < nodes[node2][2]:
                result += 1
    print(result)


if __name__ == "__main__":
    main()
