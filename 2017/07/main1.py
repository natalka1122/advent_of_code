import re

FILENAME = "demo.txt"  # expected tknk
FILENAME = "input.txt"


def main() -> None:
    nodes = set()
    not_bottom = set()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"(\w+) \(\d+\)( -> ([\w, ]+))?", line.strip())
            if line_match is None:
                print(line.strip())
                raise NotImplementedError
            nodes.add(line_match.group(1))
            if line_match.group(2) is not None:
                for node in line_match.group(3).split(", "):
                    nodes.add(node)
                    not_bottom.add(node)

    print(f"nodes = {nodes}")
    print(f"not_bottom = {not_bottom}")
    result = nodes - not_bottom
    if len(result) != 1:
        raise NotImplementedError
    print(result.pop())


if __name__ == "__main__":
    main()
