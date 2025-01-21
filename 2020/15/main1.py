FILENAME = "demo.txt"  # expected 436
FILENAME = "demo_full.txt"  # expected 436 1 10 27 78 438 1836
# FILENAME = "input.txt"

NUMBER = 2020


def f(spoken: list[int]) -> int:
    while len(spoken) < NUMBER:
        if spoken[-1] not in spoken[:-1]:
            spoken.append(0)
        else:
            spoken.append(spoken[:-1][::-1].index(spoken[-1]) + 1)
        # print(spoken)
    return spoken[NUMBER-1]

def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(list(map(int, line.strip().split(",")))))


if __name__ == "__main__":
    main()
