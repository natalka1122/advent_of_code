FILENAME = "input.txt"

GENERATIONS_COUNT = 50000000000
PLANT = "#"
MANY_STEPS = 100


def main() -> None:
    state: tuple[int, ...] = tuple([])
    transform: dict[tuple[bool, bool, bool, bool, bool], bool] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            if "initial state" in line:
                if len(state) != 0:
                    raise NotImplementedError
                plant_line: str = line.strip().split(" ")[2]
                state = tuple(filter(lambda x: plant_line[x] == PLANT, range(len(plant_line))))
            elif len(line) > 1:
                line_split = line.strip().split(" ")
                condition = tuple(map(lambda x: x == PLANT, line_split[0]))
                if condition in transform:
                    raise NotImplementedError
                if len(condition) != 5:
                    raise NotImplementedError
                transform[condition] = line_split[2] == PLANT
    visited = [(len(state), sum(state))]
    counter_on = False
    counter = 0
    diff_sum = 0
    for step in range(GENERATIONS_COUNT):
        print(f"step = {step}")
        next_state = []
        for i in range(state[0] - 2, state[-1] + 3):
            condition = tuple(map(lambda x: x in state, range(i - 2, i + 3)))
            if len(condition) != 5:
                raise NotImplementedError
            if condition in transform and transform[condition]:
                next_state.append(i)
        state = tuple(next_state)
        if visited[-1][0] == len(state):
            visited.append((len(state), sum(state)))
            if not counter_on:
                counter_on = True
                print("start timer")
            elif counter < MANY_STEPS:
                if diff_sum == 0:
                    diff_sum = visited[-1][1] - visited[-2][1]
                    print(f"updated diff_sum")
                else:
                    counter += 1
                    if visited[-1][1] - visited[-2][1] != diff_sum:
                        counter_on = False
                        print("stop timer, case 2")
                        counter = 0
                        diff_sum = 0
            else:
                break
        else:
            visited.append((len(state), sum(state)))
            if counter_on:
                counter_on = False
                print("stop timer, case 1")
                counter = 0
                diff_sum = 0
    if diff_sum == 0:
        print(sum(state))
    else:
        print(len(visited), diff_sum)
        print(visited[-1][1] + diff_sum * (GENERATIONS_COUNT - len(visited) + 1))


if __name__ == "__main__":
    main()
