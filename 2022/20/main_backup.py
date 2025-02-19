# from __future__ import annotations

FILENAME = "demo.txt"  # expected 3
FILENAME = "demo1.txt"  # expected ?
FILENAME = "demo2.txt"  # expected ?
FILENAME = "input.txt"


LOOK_AT = (1000, 2000, 3000)
ZERO = 0


def main() -> None:
    the_line = []
    result = []
    with open(FILENAME, "r") as file:
        for line in file:
            the_line.append(int(line))
            result.append(the_line[-1])
    if len(set(the_line)) != len(the_line):
        print(len(set(the_line)), len(the_line))
        raise NotImplementedError
    for index in range(len(the_line)):
        symbol = the_line[index]
        symbol_pos = result.index(symbol)
        new_symbol_pos = (symbol_pos + symbol) % (len(result) - 1)
        # if new_symbol_pos == 0:
        #     new_symbol_pos = len(result) - 1
        if new_symbol_pos < symbol_pos:
            # print(f"{symbol}: {symbol_pos} -> {new_symbol_pos}")
            result = (
                result[:new_symbol_pos]
                + [symbol]
                + result[new_symbol_pos:symbol_pos]
                + result[symbol_pos + 1 :]
            )
        elif symbol_pos < new_symbol_pos:
            # print(f"{symbol}: {symbol_pos} -> {new_symbol_pos}")
            result = (
                result[:symbol_pos]
                + result[symbol_pos + 1 : new_symbol_pos + 1]
                + [symbol]
                + result[new_symbol_pos + 1 :]
            )
        print(result)
    index0 = result.index(ZERO)
    print(
        result[(index0 + LOOK_AT[0]) % len(result)],
        result[(index0 + LOOK_AT[1]) % len(result)],
        result[(index0 + LOOK_AT[2]) % len(result)],
    )
    print(
        result[(index0 + LOOK_AT[0]) % len(result)]
        + result[(index0 + LOOK_AT[1]) % len(result)]
        + result[(index0 + LOOK_AT[2]) % len(result)]
    )


if __name__ == "__main__":
    main()
