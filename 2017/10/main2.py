from functools import reduce

FILENAME = "demo2_1.txt"  # expected a2582a3a0e66e6e86e3812dcb672a272
FILENAME = "demo2_2.txt"  # expected 33efeb34ea91902bb2f59c9920caa6cd
FILENAME = "demo2_3.txt"  # expected 3efbe78a8d82f29979031a4aa0b16a9d
FILENAME = "demo2_4.txt"  # expected 63960835bcdc130f0b66d7ff4f6a5a8e
FILENAME = "input.txt"

LIST_SIZE = 256
ROUND_COUNT = 64
SIXTEEN = 16
ADD_SEQUENCE = (17, 31, 73, 47, 23)


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
        result = result[:length][::-1] + result[length:]
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
    sparse_hash: list[int] = [x for x in range(LIST_SIZE)]
    with open(FILENAME, "r") as file:
        for line in file:
            lengths = tuple(map(ord, line.strip())) + ADD_SEQUENCE
    print(f"lengths = {lengths}")
    skip_size = 0
    current_position = 0
    for _ in range(ROUND_COUNT):
        for length in lengths:
            sparse_hash, current_position = f(sparse_hash, current_position, length, skip_size)
            skip_size += 1
    dense_hash = []
    for i in range(SIXTEEN):
        dense_hash.append(reduce(lambda x, y: x ^ y, sparse_hash[i * SIXTEEN : (i + 1) * SIXTEEN]))
    for i in range(len(dense_hash)):
        print(hex(dense_hash[i]).split("x")[1].zfill(2), end="")
    print()


if __name__ == "__main__":
    main()
