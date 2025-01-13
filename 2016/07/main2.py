import re

FILENAME = "demo2.txt"  # expected 3
FILENAME = "input.txt"


def f(line: str) -> bool:
    outside = list()
    inside = list()
    is_outside = True
    current = ""
    for symbol in line:
        if symbol == "[":
            if not is_outside:
                raise NotImplementedError
            outside.append(current)
            current = ""
            is_outside = False
        elif symbol == "]":
            if is_outside:
                raise NotImplementedError
            inside.append(current)
            current = ""
            is_outside = True
        elif "a" <= symbol <= "z":
            current += symbol
        else:
            raise NotImplementedError
    if not outside:
        raise NotImplementedError
    if current:
        outside.append(current)
    big_line = "_".join(outside) + "!" + "_".join(inside)
    big_line_match = re.search(r"([a-z])(?!\1)([a-z])\1.*!.*\2\1\2", big_line)
    return big_line_match is not None


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if f(line.strip()):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
