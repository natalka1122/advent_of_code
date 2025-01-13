import itertools

FILENAME, STORE = "demo.txt", 25  # expected 4
FILENAME, STORE = "input.txt", 150


def main() -> None:
    containers: list[int] = list()
    with open(FILENAME, "r") as file:
        for line in file:
            containers.append(int(line))
    print(containers)
    result = 0
    for count in range(1, len(containers)):
        for combination in itertools.combinations(containers, count):
            if sum(combination) == STORE:
                print(combination)
                result += 1
    print(result)


if __name__ == "__main__":
    main()
