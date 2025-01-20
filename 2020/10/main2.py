FILENAME = "demo1.txt"  # expected 8
FILENAME = "demo2.txt"  # expected 19208
FILENAME = "input.txt"


def f(x: int) -> int:
    if x == 0:
        return 1
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    if x == 4:
        print("bip")
        return 7
    print(f"x = {x}")
    raise NotImplementedError


def main() -> None:
    jolts: list[int] = [0]
    with open(FILENAME, "r") as file:
        for line in file:
            jolts.append(int(line))
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    print(jolts)
    value1 = 0
    result = 1
    for i in range(len(jolts) - 1):
        if jolts[i + 1] - jolts[i] == 1:
            value1 += 1
        elif jolts[i + 1] - jolts[i] == 3:
            result = result * f(value1)
            value1 = 0
        else:
            raise NotImplementedError
    print(result)


if __name__ == "__main__":
    main()
