from bisect import bisect_left

# FILENAME = "demo.txt"  # expected 3
FILENAME = "input.txt"

DASH = "-"


def add_to_range(id1: int, id2: int, ranges: list[int]) -> None:
    index1 = bisect_left(ranges, id1)
    index2 = bisect_left(ranges, id2)
    if index1 == index2:
        if index1 % 2 == 0:
            ranges.insert(index1, id1)
            ranges.insert(index1 + 1, id2)
    elif index1 % 2 == 0:
        if index2 % 2 == 0:
            ranges[index1] = id1
            ranges[index2 - 1] = id2
            for _ in range(index1 + 1, index2 - 1):
                ranges.pop(index1 + 1)
        else:
            ranges[index1] = id1
            for _ in range(index1 + 1, index2):
                ranges.pop(index1 + 1)
    else:
        if index2 % 2 == 0:
            ranges[index2 - 1] = id2
            for _ in range(index1 + 1, index2):
                ranges.pop(index1)
        else:
            for _ in range(index1, index2):
                ranges.pop(index1)


def check(id: int, ranges: list[int]) -> bool:
    index = bisect_left(ranges, id)
    if index == len(ranges):
        return False
    if index % 2 == 0:
        if id < ranges[index]:
            return False
        elif id == ranges[index]:
            return True
        else:
            print("CASE 02")
            raise NotImplementedError
    else:
        if id < ranges[index]:
            return True
        elif id == ranges[index]:
            return False
        else:
            print("CASE 12")
            raise NotImplementedError


def main() -> None:
    result: list[int] = []
    ranges: list[int] = []
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.rstrip("\n")
            if len(line) == 0:
                continue
            if DASH in line:
                id1, id2 = line.split(DASH)
                add_to_range(int(id1), int(id2) + 1, ranges)
            elif check(int(line), ranges):
                result.append(int(line))
    print(len(result))


if __name__ == "__main__":
    main()
