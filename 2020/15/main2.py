FILENAME, NUMBER = "demo.txt", 10  # expected 0
FILENAME, NUMBER = "demo.txt", 2020  # expected 436
FILENAME, NUMBER = "demo.txt", 30000000  # expected 175594
FILENAME, NUMBER = "demo_full.txt", 2020  # expected 436 1 10 27 78 438 1836
FILENAME, NUMBER = "demo_full.txt", 30000000  # expected 175594 2578 3544142 261214 6895259 18 362
FILENAME, NUMBER = "input.txt", 30000000


def f(spoken_list: list[int]) -> int:
    spoken = dict()
    for index, value in enumerate(spoken_list):
        spoken[value] = index
    index = len(spoken)
    last_index = None
    while index < NUMBER:
        if last_index is None:
            next_spoken = 0
        else:
            next_spoken = index - last_index - 1
        if next_spoken in spoken:
            last_index = spoken[next_spoken]
            spoken[next_spoken] = index
        else:
            last_index = None
            spoken[next_spoken] = index
        # print(
        #     f"index = {index}",
        #     f"last_one = {last_one}",
        #     f"last_index = {last_index}",
        #     f"next_spoken = {next_spoken}",
        #     f"spoken = {spoken}",
        # )
        index += 1
    return next_spoken


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(list(map(int, line.strip().split(",")))))


if __name__ == "__main__":
    main()
