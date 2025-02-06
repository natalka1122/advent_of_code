FILENAME = "demo.txt"  # expected 1
FILENAME = "input.txt"

Quadriple = tuple[int, int, int, int]


def addr(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = values[instruction[1]] + values[instruction[2]]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def addi(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = values[instruction[1]] + instruction[2]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def mulr(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = values[instruction[1]] * values[instruction[2]]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def muli(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = values[instruction[1]] * instruction[2]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def banr(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = values[instruction[1]] & values[instruction[2]]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def bani(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = values[instruction[1]] & instruction[2]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def borr(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = values[instruction[1]] | values[instruction[2]]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def bori(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = values[instruction[1]] | instruction[2]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def setr(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = values[instruction[1]]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def seti(values: Quadriple, instruction: Quadriple) -> Quadriple:
    value = instruction[1]
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def gtir(values: Quadriple, instruction: Quadriple) -> Quadriple:
    if instruction[1] > values[instruction[2]]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def gtri(values: Quadriple, instruction: Quadriple) -> Quadriple:
    if values[instruction[1]] > instruction[2]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def gtrr(values: Quadriple, instruction: Quadriple) -> Quadriple:
    if values[instruction[1]] > values[instruction[2]]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def eqir(values: Quadriple, instruction: Quadriple) -> Quadriple:
    if instruction[1] == values[instruction[2]]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def eqri(values: Quadriple, instruction: Quadriple) -> Quadriple:
    if values[instruction[1]] == instruction[2]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def eqrr(values: Quadriple, instruction: Quadriple) -> Quadriple:
    if values[instruction[1]] == values[instruction[2]]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[3]] + (value,) + values[instruction[3] + 1 :]
    if len(result) != 4:
        raise NotImplementedError
    return result


def f(
    begin_values: Quadriple,
    instruction: Quadriple,
    after_values: Quadriple,
) -> bool:
    result = 0
    for func in [
        addr,
        addi,
        mulr,
        muli,
        banr,
        bani,
        borr,
        bori,
        setr,
        seti,
        gtir,
        gtri,
        gtrr,
        eqir,
        eqri,
        eqrr,
    ]:
        if func(begin_values, instruction) == after_values:
            result += 1
    print(result)
    return result >= 3


def main() -> None:
    result = 0
    next_begin = True
    next_four = False
    next_after = False
    next_empty = False
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if next_begin:
                if line.startswith("Before"):
                    v = tuple(map(int, line[9:-1].split(", ")))
                    if len(v) != 4:
                        raise NotImplementedError
                    begin_values = v
                    next_begin = False
                    next_four = True
                elif len(line) == 0:
                    break
                else:
                    raise NotImplementedError
            elif next_four:
                if len(line) > 0:
                    v = tuple(map(int, line.split(" ")))
                    if len(v) != 4:
                        raise NotImplementedError
                    instruction = v
                    next_four = False
                    next_after = True
                else:
                    raise NotImplementedError
            elif next_after:
                if line.startswith("After"):
                    v = tuple(map(int, line[9:-1].split(", ")))
                    if len(v) != 4:
                        raise NotImplementedError
                    after_values = v
                    next_after = False
                    next_empty = True
                    if f(begin_values, instruction, after_values):
                        result += 1
                else:
                    raise NotImplementedError
            elif next_empty:
                next_empty = False
                next_begin = True
            else:
                raise NotImplementedError
    print(result)


if __name__ == "__main__":
    main()
