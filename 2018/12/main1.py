FILENAME = "demo.txt"  # exoected 325
FILENAME = "input.txt"

GENERATIONS_COUNT = 20
PLANT = "#"


def main() -> None:
    initial_state: set[int] | None = None
    transform: dict[tuple[bool, bool, bool, bool, bool], bool] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            if "initial state" in line:
                if initial_state is not None:
                    raise NotImplementedError
                plant_line: str = line.strip().split(" ")[2]
                initial_state = set(
                    filter(lambda x: plant_line[x] == PLANT, range(len(plant_line)))
                )
            elif len(line) > 1:
                line_split = line.strip().split(" ")
                condition = tuple(map(lambda x: x == PLANT, line_split[0]))
                if condition in transform:
                    raise NotImplementedError
                if len(condition) != 5:
                    raise NotImplementedError
                transform[condition] = line_split[2] == PLANT
    if initial_state is None:
        raise NotImplementedError
    state = initial_state
    for _ in range(GENERATIONS_COUNT):
        next_state = set()
        for i in range(min(state) - 2, max(state) + 3):
            condition = tuple(map(lambda x: x in state, range(i - 2, i + 3)))
            if len(condition) != 5:
                raise NotImplementedError
            if condition in transform and transform[condition]:
                next_state.add(i)
        state = next_state
    print(sum(next_state))


if __name__ == "__main__":
    main()
