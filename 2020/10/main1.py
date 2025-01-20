FILENAME = "demo1.txt"  # expected 35
FILENAME = "demo2.txt"  # expected 220
FILENAME = "input.txt"


def main() -> None:
    jolts: list[int] = []
    with open(FILENAME, "r") as file:
        for line in file:
            jolts.append(int(line))
    jolts.sort()
    value1 = 0
    value3 = 0
    for i in range(len(jolts) - 1):
        if jolts[i + 1] - jolts[i] == 0:
            raise NotImplementedError
        elif jolts[i + 1] - jolts[i] == 1:
            value1 += 1
        elif jolts[i + 1] - jolts[i] == 3:
            value3 += 1
        else:
            raise NotImplementedError
    print(value1, value3)
    print((value1 + 1) * (value3 + 1))


if __name__ == "__main__":
    main()
