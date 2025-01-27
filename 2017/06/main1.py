FILENAME = "demo.txt"  # expected 5
# FILENAME = "input.txt"


def main() -> None:
    state_list: list[tuple[int, ...]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            state_list.append(tuple(map(int, line.strip().replace("\t", " ").split(" "))))
    print(state_list)
    while True:
        next_state = list(state_list[-1])
        max_bank = max(next_state)
        max_bank_index = next_state.index(max_bank)
        next_state[max_bank_index] = 0
        for i in range(max_bank):
            next_state[(max_bank_index + 1 + i) % len(next_state)] += 1
        next_state_tuple = tuple(next_state)
        if next_state_tuple in state_list:
            break
        else:
            state_list.append(next_state_tuple)
    print(len(state_list))


if __name__ == "__main__":
    main()
