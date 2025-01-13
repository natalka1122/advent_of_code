FILENAME = "input.txt"
LETTERS = "abcd"
CPY = "cpy"
INC = "inc"
DEC = "dec"
JNZ = "jnz"
NIL = "nil"
ADD = "add"
MUL = "mul"
OUT = "out"

Values = tuple[int, int, int, int]
Program = list[list[str | int]]


def cpy(values: Values, index: int, program: Program) -> tuple[Values, int]:
    current = program[index]
    if current[0] != CPY or len(current) != 3:
        raise NotImplementedError
    if isinstance(current[2], int):
        print(f"toggling produces an invalid instruction {current}, continue")
        return values, index
    if isinstance(current[1], int):
        src_value = current[1]
    elif current[1] in LETTERS:
        src_value = values[LETTERS.index(current[1])]
    else:
        raise NotImplementedError
    if current[2] not in LETTERS:
        raise NotImplementedError
    target_index = LETTERS.index(current[2])
    new_values = values[:target_index] + (src_value,) + values[target_index + 1 :]
    if len(new_values) != 4:
        raise NotImplementedError
    new_index = index + 1
    return new_values, new_index


def inc(values: Values, index: int, program: Program) -> tuple[Values, int]:
    current = program[index]
    if current[0] != INC or len(current) != 2:
        raise NotImplementedError
    if isinstance(current[1], int):
        print(f"toggling produces an invalid instruction {current}, continue")
        return values, index
    if current[1] not in LETTERS:
        raise NotImplementedError
    target_index = LETTERS.index(current[1])
    new_values = (
        values[:target_index] + (values[target_index] + 1,) + values[target_index + 1 :]
    )
    if len(new_values) != 4:
        raise NotImplementedError
    new_index = index + 1
    return new_values, new_index


def dec(values: Values, index: int, program: Program) -> tuple[Values, int]:
    current = program[index]
    if current[0] != DEC or len(current) != 2:
        raise NotImplementedError
    if isinstance(current[1], int):
        print(f"toggling produces an invalid instruction {current}, continue")
        return values, index
    if current[1] not in LETTERS:
        raise NotImplementedError
    target_index = LETTERS.index(current[1])
    new_values = (
        values[:target_index] + (values[target_index] - 1,) + values[target_index + 1 :]
    )
    if len(new_values) != 4:
        raise NotImplementedError
    new_index = index + 1
    return new_values, new_index


def jnz(values: Values, index: int, program: Program) -> tuple[Values, int]:
    current = program[index]
    if current[0] != JNZ or len(current) != 3:
        raise NotImplementedError
    if isinstance(current[1], int):
        check_value = current[1]
    elif current[1] in LETTERS:
        check_value = values[LETTERS.index(current[1])]
    else:
        raise NotImplementedError
    if check_value == 0:
        return values, index + 1
    if isinstance(current[2], int):
        jump_value = current[2]
    elif current[2] in LETTERS:
        jump_value = values[LETTERS.index(current[2])]
    else:
        raise NotImplementedError
    if program[index + jump_value][0] in [NIL, MUL, ADD]:
        raise NotImplementedError
    return values, index + jump_value


def out(values: Values, index: int, program: Program) -> tuple[Values, int, int]:
    current = program[index]
    if current[0] != OUT or len(current) != 2:
        raise NotImplementedError
    if isinstance(current[1], int):
        target_index = current[1]
    else:
        target_index = LETTERS.index(current[1])
    return values, index + 1, values[target_index]


def nil(values: Values, index: int, program: Program) -> tuple[Values, int]:
    current = program[index]
    if current[0] != NIL or len(current) != 1:
        raise NotImplementedError
    return values, index + 1


def add(values: Values, index: int, program: Program) -> tuple[Values, int]:
    current = program[index]
    if current[0] != ADD or len(current) != 3:
        raise NotImplementedError
    if isinstance(current[1], int) or isinstance(current[2], int):
        raise NotImplementedError
    if current[1] not in LETTERS or current[2] not in LETTERS:
        raise NotImplementedError
    source_index = LETTERS.index(current[1])
    destination_index = LETTERS.index(current[2])
    if source_index < destination_index:
        new_values = (
            values[:source_index]
            + (0,)
            + values[source_index + 1 : destination_index]
            + (values[source_index] + values[destination_index],)
            + values[destination_index + 1 :]
        )
    elif source_index > destination_index:
        new_values = (
            values[:destination_index]
            + (values[source_index] + values[destination_index],)
            + values[destination_index + 1 : source_index]
            + (0,)
            + values[source_index + 1 :]
        )
    else:
        raise NotImplementedError
    if len(new_values) != 4:
        print(
            f"values = {values} source_index = {source_index} destination_index = {destination_index} new_values = {new_values}"
        )
        raise NotImplementedError
    return new_values, index + 1


def mul(values: Values, index: int, program: Program) -> tuple[Values, int]:
    current = program[index]
    if current[0] != MUL or len(current) != 5:
        raise NotImplementedError
    values_list = list(values)
    if (
        isinstance(current[2], int)
        or isinstance(current[3], int)
        or isinstance(current[4], int)
    ):
        raise NotImplementedError
    if isinstance(current[1], int):
        x = current[1]
    else:
        x = values_list[LETTERS.index(current[1])]
    values_list[LETTERS.index(current[3])] += x * values_list[LETTERS.index(current[4])]
    values_list[LETTERS.index(current[2])] = 0
    values_list[LETTERS.index(current[4])] = 0
    new_values = tuple(values_list)
    if len(new_values) != 4:
        raise NotImplementedError
    return new_values, index + 1


def simplify_program(program: Program) -> None:
    changed = False
    for index, command in enumerate(program):
        if command[0] == JNZ and command[2] == -2 and index >= 2:
            if (
                program[index - 1][0] == INC
                and program[index - 2][0] == DEC
                and command[1] == program[index - 2][1]
            ):
                program[index] = [ADD, program[index - 2][1], program[index - 1][1]]
                program[index - 1] = [NIL]
                program[index - 2] = [NIL]
                changed = True
                break
            if (
                program[index - 1][0] == DEC
                and program[index - 2][0] == INC
                and command[1] == program[index - 1][1]
            ):
                program[index] = [ADD, program[index - 1][1], program[index - 2][1]]
                program[index - 1] = [NIL]
                program[index - 2] = [NIL]
                changed = True
                break
        if command[0] == JNZ and command[2] == -5 and index >= 5:
            if (
                program[index - 5][0] == CPY
                and program[index - 4][0] == NIL
                and program[index - 3][0] == NIL
                and program[index - 2][0] == ADD
                and program[index - 1][0] == DEC
                and program[index - 5][2] == program[index - 2][1]
                and program[index - 1][1] == command[1]
            ):
                program[index] = [
                    MUL,
                    program[index - 5][1],
                    program[index - 5][2],
                    program[index - 2][2],
                    program[index - 1][1],
                ]
                program[index - 1] = [NIL]
                program[index - 2] = [NIL]
                program[index - 5] = [NIL]
                changed = True
                break

    if changed:
        print(f"new_program:")
        print("\n".join(map(lambda x: str(x), program)))
        return simplify_program(program)


def get_next_out(
    values: Values, index: int, program: Program
) -> tuple[Values, int, int]:
    while 0 <= index < len(program):
        current = program[index]
        if current[0] == CPY:
            values, index = cpy(values, index, program)
        elif current[0] == INC:
            values, index = inc(values, index, program)
        elif current[0] == DEC:
            values, index = dec(values, index, program)
        elif current[0] == JNZ:
            values, index = jnz(values, index, program)
        elif current[0] == NIL:
            values, index = nil(values, index, program)
        elif current[0] == ADD:
            values, index = add(values, index, program)
        elif current[0] == MUL:
            values, index = mul(values, index, program)
        elif current[0] == OUT:
            return out(values, index, program)
        else:
            raise NotImplementedError
    raise NotImplementedError


def main() -> None:
    program: Program = []
    with open(FILENAME, "r") as file:
        for line in file:
            line_split = list(
                map(
                    lambda x: int(x) if x.isdigit() or x[1:].isdigit() else x,
                    line.strip().split(" "),
                )
            )
            program.append(line_split)
    print(program)
    simplify_program(program)
    start_a = 1
    is_good = False
    while not is_good:
        print(f"start_a = {start_a}", end=" ")
        values = start_a, 0, 0, 0
        values, index, first_out = get_next_out(values, 0, program)
        is_good = True
        for i in range(1000):
            values, index, current_out = get_next_out(values, index, program)
            if i % 2 == 0 and current_out != 1 - first_out:
                is_good = False
                break
            elif i % 2 == 1 and current_out != first_out:
                is_good = False
                break
        if is_good:
            print(f"result = {start_a}")
        else:
            print(f"i = {i}")
        start_a += 1


if __name__ == "__main__":
    main()
