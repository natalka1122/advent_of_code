import itertools
import math

FILENAME = "demo.txt"  # expected 99
FILENAME = "input.txt"


def main() -> None:
    packages = []
    with open(FILENAME, "r") as file:
        for line in file:
            packages.append(int(line.strip()))
    print(packages)
    total_weight = sum(packages)
    if total_weight % 3 != 0:
        raise NotImplementedError
    group_weight = total_weight // 3
    found_it = False
    result = None
    for num in range(len(packages) - 2):
        for group in itertools.combinations(packages, num):
            if sum(group) == group_weight:
                found_it = True
                print(group)
                current = math.prod(group)
                if result is None or result > current:
                    result = current
        if found_it:
            break
    print(result)


if __name__ == "__main__":
    main()
