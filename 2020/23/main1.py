FILENAME, MOVE_COUNT = "demo.txt", 1  # expected ?
FILENAME, MOVE_COUNT = "demo.txt", 10  # expected 92658374
FILENAME, MOVE_COUNT = "demo.txt", 100  # expected 67384529
FILENAME, MOVE_COUNT = "input.txt", 100

ONE = 1


def f(cups: tuple[int, ...]) -> tuple[int, ...]:
    current_cup_value = cups[0]
    destination_cup_value = current_cup_value - 1 if current_cup_value > 1 else 9
    destination_cup_index = cups.index(destination_cup_value)
    # print(
    #     f"current_cup_value = {current_cup_value}",
    #     f"destination_cup_value = {destination_cup_value}",
    #     f"destination_cup_index = {destination_cup_index}",
    # )
    while 1 <= destination_cup_index <= 3:
        destination_cup_value = destination_cup_value - 1 if destination_cup_value > 1 else 9
        destination_cup_index = cups.index(destination_cup_value)
        # print(
        #     f"destination_cup_value = {destination_cup_value}",
        #     f"destination_cup_index = {destination_cup_index}",
        # )
    return (
        cups[4 : destination_cup_index + 1]
        + cups[1:4]
        + cups[destination_cup_index + 1 :]
        + cups[:1]
    )


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            cups = tuple(map(lambda x: int(x), line))
            for i in range(MOVE_COUNT):
                cups = f(cups)
                # print(i, ":", cups)
    index = cups.index(ONE)
    print("".join(map(str, cups[index + 1 :] + cups[:index])))


if __name__ == "__main__":
    main()
