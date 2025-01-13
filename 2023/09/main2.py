from __future__ import annotations

# FILENAME = "demo.txt"
# FILENAME = "demo1.txt"
# FILENAME = "demo2.txt"
FILENAME = "input.txt"


def f(values):
    next_lines = [values]
    while any(value != 0 for value in next_lines[-1]):
        next_lines.append([])
        for i in range(len(next_lines[-2]) - 1):
            next_lines[-1].append(next_lines[-2][i + 1] - next_lines[-2][i])
    for index in range(len(next_lines) - 2, -1, -1):
        next_lines[index].append(next_lines[index][0] - next_lines[index + 1][-1])
    return values[-1]


def main():
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(list(map(int, line.split(" "))))
    print(result)


if __name__ == "__main__":
    main()
