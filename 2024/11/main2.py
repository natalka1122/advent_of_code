import functools

FILENAME, MAX_STEPS = "demo.txt", 1  # expected 3
FILENAME, MAX_STEPS = "demo.txt", 2  # expected 4
FILENAME, MAX_STEPS = "demo.txt", 3  # expected 5
FILENAME, MAX_STEPS = "demo.txt", 4  # expected 9
FILENAME, MAX_STEPS = "demo.txt", 5  # expected 13
FILENAME, MAX_STEPS = "demo.txt", 6  # expected 22
FILENAME, MAX_STEPS = "demo.txt", 25  # expected 55312
FILENAME, MAX_STEPS = "input.txt", 25
FILENAME, MAX_STEPS = "input.txt", 75


@functools.cache
def f(elem, count) -> int:
    if count == 0:
        return 1
    if elem == 0:
        return f(1, count - 1)
    elem_str = str(elem)
    if len(elem_str) % 2 == 0:
        return f(int(elem_str[: len(elem_str) // 2]), count - 1) + f(
            int(elem_str[len(elem_str) // 2 :]), count - 1
        )
    else:
        return f(elem * 2024, count - 1)


def main():
    with open(FILENAME, "r") as file:
        line = list(map(int, file.readline().split(" ")))
    result = 0
    for elem in line:
        result += f(elem, MAX_STEPS)
    print(result)


if __name__ == "__main__":
    main()
