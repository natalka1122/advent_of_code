from typing import Any
import json

# FILENAME = "demo2.txt"
FILENAME = "input.txt"
RED = "red"


def f(line: list[Any] | dict[str, Any]) -> int:
    if isinstance(line, list):
        result = 0
        for elem in line:
            result += f(elem)
        return result
    elif isinstance(line, dict):
        if RED in line.values():
            return 0
        result = 0
        for elem in line.values():
            result += f(elem)
        return result
    elif isinstance(line, int):
        return line
    elif isinstance(line, str):
        return 0
    else:
        print(type(line), line)
        raise NotImplementedError


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(json.loads(line.strip())))


if __name__ == "__main__":
    main()
