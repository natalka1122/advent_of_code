import re

FILENAME = "demo1.txt"  # expected 2
# FILENAME = "input.txt"


def check(line: str) -> bool:
    line_match = re.search(r"([a-z])([a-z])\2\1", line)
    if line_match is None:
        return False
    return line_match.group(1) != line_match.group(2)


def f(line: str) -> bool:
    outside = set()
    is_outside = True
    current = ""
    for symbol in line:
        if symbol == "[":
            if not is_outside:
                raise NotImplementedError
            outside.add(check(current))
            current = ""
            is_outside = False
        elif symbol == "]":
            if is_outside:
                raise NotImplementedError
            if check(current):
                return False
            current = ""
            is_outside = True
        elif "a" <= symbol <= "z":
            current += symbol
        else:
            raise NotImplementedError
    if not outside:
        raise NotImplementedError
    if current:
        outside.add(check(current))
    return any(outside)


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            if f(line.strip()):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
