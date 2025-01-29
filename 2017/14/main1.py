from functools import reduce

FILENAME = "demo.txt"  # expected 8108
FILENAME = "input.txt"

SIZE = 128
LIST_SIZE = 256
ROUND_COUNT = 64
SIXTEEN = 16
ADD_SEQUENCE = [17, 31, 73, 47, 23]


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


def knot_hash(lengths: list[int]) -> int:
    sparse_hash: list[int] = [x for x in range(LIST_SIZE)]
    skip_size = 0
    current_position = 0
    for _ in range(ROUND_COUNT):
        for length in lengths + ADD_SEQUENCE:
            sparse_hash, current_position = f(sparse_hash, current_position, length, skip_size)
            skip_size += 1
    dense_hash = []
    for i in range(SIXTEEN):
        dense_hash.append(reduce(lambda x, y: x ^ y, sparse_hash[i * SIXTEEN : (i + 1) * SIXTEEN]))
    # print(dense_hash)
    result = 0
    for num in dense_hash:
        result += bin(num)[2:].count("1")
    #     print(bin(num)[2:].zfill(8), end="")
    # print()
    return result


def main() -> None:
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
    result = 0
    for i in range(SIZE):
        current_line = f"{line}-{i}"
        result += knot_hash(list(map(ord, current_line)))
    print(result)


if __name__ == "__main__":
    main()
