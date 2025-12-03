# FILENAME = "demo.txt"
FILENAME = "input.txt"


class NotFoundError(Exception):
    """NotFoundError"""


def f(line: list[int], length: int) -> int:
    if length <= 0:
        raise NotImplementedError
    for num in range(9, 0, -1):
        try:
            first_index = line[: len(line) - length + 1].index(num)
        except ValueError:
            continue
        if length == 1:
            return num
        try:
            rest_value = f(line[first_index + 1 :], length - 1)
        except NotFoundError:
            continue
        result = num * 10 ** (length - 1) + rest_value
        return result
    raise NotFoundError


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(list(map(int, line.strip())), 12)
    print(result)


if __name__ == "__main__":
    main()
