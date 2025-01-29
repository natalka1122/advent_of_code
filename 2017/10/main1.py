FILENAME, LIST_SIZE = "demo1.txt", 5  # expected 12
FILENAME, LIST_SIZE = "input.txt", 256


def f(
    the_list: list[int], current_position: int, length: int, skip_size: int
) -> tuple[list[int], int]:
    if current_position + length <= len(the_list):
        result = (
            the_list[:current_position]
            + the_list[current_position : current_position + length][::-1]
            + the_list[current_position + length :]
        )
    else:
        # lazy option
        result = the_list[current_position:] + the_list[:current_position]
        result = result[: length][::-1] + result[length :]
        result = result[-current_position:] + result[:-current_position]
        # extra = current_position + length - len(the_list)
        # result = (
        #     the_list[current_position : current_position + extra][::-1]
        #     + the_list[extra:current_position]
        #     + the_list[:extra][::-1]
        #     + the_list[current_position + extra :][::-1]
        # )
    return result, (current_position + length + skip_size) % len(the_list)


def main() -> None:
    the_list: list[int] = [x for x in range(LIST_SIZE)]
    with open(FILENAME, "r") as file:
        for line in file:
            lengths = tuple(map(int, line.strip().split(",")))
    print(lengths)
    skip_size = 0
    current_position = 0
    for length in lengths:
        the_list, current_position = f(the_list, current_position, length, skip_size)
        skip_size += 1
    print(the_list[0] * the_list[1])


if __name__ == "__main__":
    main()
