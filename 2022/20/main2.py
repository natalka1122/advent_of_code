FILENAME = "demo.txt"  # expected 1623178306
FILENAME = "input.txt"


LOOK_AT = (1000, 2000, 3000)
ZERO = 0
DECRYPTION_KEY = 811589153
MIX_COUNT = 10


def main() -> None:
    the_line = []
    result = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_line.append(int(line) * DECRYPTION_KEY)
    result = list(enumerate(the_line))
    for _ in range(MIX_COUNT):
        for index in range(len(the_line)):
            symbol = the_line[index]
            symbol_pos = result.index((index, symbol))
            new_symbol_pos = (symbol_pos + symbol) % (len(result) - 1)
            if new_symbol_pos < symbol_pos:
                # print(f"{symbol}: {symbol_pos} -> {new_symbol_pos}")
                result = (
                    result[:new_symbol_pos]
                    + result[symbol_pos : symbol_pos + 1]
                    + result[new_symbol_pos:symbol_pos]
                    + result[symbol_pos + 1 :]
                )
            elif symbol_pos < new_symbol_pos:
                # print(f"{symbol}: {symbol_pos} -> {new_symbol_pos}")
                result = (
                    result[:symbol_pos]
                    + result[symbol_pos + 1 : new_symbol_pos + 1]
                    + result[symbol_pos : symbol_pos + 1]
                    + result[new_symbol_pos + 1 :]
                )
            # print(result)
    index_line = the_line.index(ZERO)
    index_result = result.index((index_line, ZERO))
    print(
        result[(index_result + LOOK_AT[0]) % len(result)],
        result[(index_result + LOOK_AT[1]) % len(result)],
        result[(index_result + LOOK_AT[2]) % len(result)],
    )
    print(
        result[(index_result + LOOK_AT[0]) % len(result)][1]
        + result[(index_result + LOOK_AT[1]) % len(result)][1]
        + result[(index_result + LOOK_AT[2]) % len(result)][1]
    )


if __name__ == "__main__":
    main()
