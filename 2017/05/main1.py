FILENAME = "demo.txt"  # expected 5
FILENAME = "input.txt"


def main() -> None:
    instructions = []
    with open(FILENAME, "r") as file:
        for line in file:
            instructions.append(int(line))
    step = 0
    index = 0
    while 0 <= index < len(instructions):
        step += 1
        new_index = index + instructions[index]
        instructions[index] += 1
        index = new_index
    print(step)


if __name__ == "__main__":
    main()
