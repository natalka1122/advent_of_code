from __future__ import annotations

# FILENAME = "demo.txt"  # expected 2858
# FILENAME = "demo1.txt"
# FILENAME = "demo2.txt"
FILENAME = "input.txt"
EMPTY = "."


def main():
    with open(FILENAME, "r") as file:
        line = list(
            map(
                lambda x: (int(x[1]), int(x[0]) // 2 if int(x[0]) % 2 == 0 else "."),
                enumerate(file.readline().strip()),
            )
        )
    line = list(filter(lambda x: x[0] > 0, line))
    print(line)
    right = len(line) - 1
    while right > 0:
        if line[right][1] == EMPTY:
            right -= 1
        else:
            for left in range(1, right):
                if line[left][1] == EMPTY and line[left][0] >= line[right][0]:
                    # print(f"left = {left} right = {right} line[right] = {line[right]}")
                    line = (
                        line[:left]
                        + [line[right]]
                        + [(line[left][0] - line[right][0], EMPTY)]
                        + line[left + 1 : right]
                        + [(line[right][0], EMPTY)]
                        + line[right + 1 :]
                    )
                    break
            else:
                right -= 1

    # this can be done quickler, but it works
    filesystem = []
    for key, value in line:
        filesystem.extend([value] * key)
    # print(filesystem)
    result = 0
    for key, value in enumerate(filesystem):
        if value != EMPTY:
            result += key * value
    print(result)


if __name__ == "__main__":
    main()
