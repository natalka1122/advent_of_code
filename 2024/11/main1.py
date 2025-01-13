from __future__ import annotations

FILENAME, MAX_STEPS = "demo.txt", 1  # expected 3
FILENAME, MAX_STEPS = "demo.txt", 2  # expected 4
FILENAME, MAX_STEPS = "demo.txt", 3  # expected 5
FILENAME, MAX_STEPS = "demo.txt", 4  # expected 9
FILENAME, MAX_STEPS = "demo.txt", 5  # expected 13
FILENAME, MAX_STEPS = "demo.txt", 6  # expected 22
FILENAME, MAX_STEPS = "demo.txt", 25  # expected 55312
FILENAME, MAX_STEPS = "input.txt", 25


def f(line: list[int]) -> list[int]:
    result = []
    for elem in line:
        if elem == 0:
            result.append(1)
            continue
        elem_str = str(elem)
        if len(elem_str) % 2 == 0:
            result.append(int(elem_str[: len(elem_str) // 2]))
            result.append(int(elem_str[len(elem_str) // 2 :]))
        else:
            result.append(elem * 2024)
    return result


def main():
    with open(FILENAME, "r") as file:
        line = list(map(int, file.readline().split(" ")))
    for _ in range(MAX_STEPS):
        line = f(line)
    print(len(line))


if __name__ == "__main__":
    main()
