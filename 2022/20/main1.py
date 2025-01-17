# from __future__ import annotations

FILENAME = "demo.txt"  # expected 3
# FILENAME = "demo1.txt"  # expected ?
# FILENAME = "demo2.txt"  # expected ?
FILENAME = "input.txt"


LOOK_AT = (1000, 2000, 3000)
ZERO = 0


def main() -> None:
    the_line = []
    result = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_line.append(int(line))
    result = list(enumerate(the_line))
    for index in range(len(the_line)):
        symbol = the_line[index]
        symbol_pos = result.index((index, symbol))
        new_symbol_pos = (symbol_pos + symbol) % (len(result) - 1)
        # # if new_symbol_pos == 0:
        # #     new_symbol_pos = len(result) - 1
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
    index_result = result.index((index_line,ZERO))
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
