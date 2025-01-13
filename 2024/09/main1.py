from __future__ import annotations

# FILENAME = "demo.txt" # expected 1928
# FILENAME = "demo1.txt"
# FILENAME = "demo2.txt" # expected 2132
FILENAME = "input.txt"
EMPTY = "."


def main():
    with open(FILENAME, "r") as file:
        line = file.readline()
    # print(line)
    filesystem = []
    for key, value in enumerate(line):
        filesystem.extend(
            [int(key) // 2] * int(value) if key % 2 == 0 else [EMPTY] * int(value)
        )
    print(filesystem)
    left = 0
    right = len(filesystem) - 1
    while left < right:
        if filesystem[left] != EMPTY:
            left += 1
            continue
        if filesystem[right] != EMPTY:
            filesystem[left], filesystem[right] = filesystem[right], filesystem[left]
        right -= 1

    print(filesystem)
    result = 0
    for key, value in enumerate(filesystem):
        if value == EMPTY:
            break
        result += key*value
    print(result)


if __name__ == "__main__":
    main()
