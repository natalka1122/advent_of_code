FILENAME = "input.txt"

FOUR = 4
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


OPERATIONS = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr,
}


def do_cleanup(operators_ciphered: dict[int, set[str]]) -> None:
    for key1, value1 in operators_ciphered.items():
        if len(value1) < 1:
            raise NotImplementedError
        if len(value1) > 1:
            continue
        for v1 in value1:
            changed = False
            for key2, value2 in operators_ciphered.items():
                if key1 == key2:
                    continue
                if v1 in value2:
                    value2.remove(v1)
                    changed = True
            if changed:
                return do_cleanup(operators_ciphered)


def main() -> None:
    next_begin = True
    next_four = False
    next_after = False
    next_empty = False
    next_program = False
    registers: Quadriple = (0, 0, 0, 0)
    operators_deciphered: dict[int, str] = dict()
    operators_ciphered: dict[int, set[str]] = dict()
    for opcode in range(len(OPERATIONS)):
        operators_ciphered[opcode] = set(OPERATIONS)
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
                    for opcode in range(len(OPERATIONS)):
                        if len(operators_ciphered[opcode]) != 1:
                            print(f"operators_ciphered = {operators_ciphered}")
                            raise NotImplementedError
                        for opname in operators_ciphered[opcode]:
                            operators_deciphered[opcode] = opname
                    print(f"operators_deciphered = {operators_deciphered}")
                    next_begin = False
                    next_program = True
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
                    unfit_operations = set()
                    for operation in operators_ciphered[instruction[0]]:
                        if OPERATIONS[operation](begin_values, instruction) != after_values:
                            unfit_operations.add(operation)
                    if len(unfit_operations) > 0:
                        operators_ciphered[instruction[0]] -= unfit_operations
                        if len(operators_ciphered[instruction[0]]) == 1:
                            do_cleanup(operators_ciphered)
                else:
                    raise NotImplementedError
            elif next_empty:
                next_empty = False
                next_begin = True
            elif next_program:
                if len(line) == 0:
                    continue
                line_split = tuple(map(int, line.split(" ")))
                if len(line_split) != 4:
                    raise NotImplementedError
                registers = OPERATIONS[operators_deciphered[line_split[0]]](registers, line_split)
            else:
                raise NotImplementedError
    print(registers)
    print(registers[0])


if __name__ == "__main__":
    main()
