FILENAME, START_A, START_B, START_C, START_D = "demo.txt", 0, 0, 0, 0  # expected 3
FILENAME, START_A, START_B, START_C, START_D = "input.txt", 7, 0, 0, 0  # expected 11415
FILENAME, START_A, START_B, START_C, START_D = "input.txt", 12, 0, 0, 0
LETTERS = "abcd"
CPY = "cpy"
INC = "inc"
DEC = "dec"
JNZ = "jnz"
TGL = "tgl"
NIL = "nil"
ADD = "add"
MUL = "mul"

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
    return values, index + jump_value


def tgl(values: Values, index: int, program: Program) -> tuple[Values, int]:
    current = program[index]
    if current[0] != TGL or len(current) != 2:
        raise NotImplementedError
    if isinstance(current[1], int):
        toggle_index = index + current[1]
    elif current[1] in LETTERS:
        toggle_index = index + values[LETTERS.index(current[1])]
    else:
        raise NotImplementedError
    if 0 <= toggle_index < len(program):
        print(f"toggle {toggle_index} {program[toggle_index]} {values}", end=" ")
        if (
            program[toggle_index][0] == ADD
            or program[toggle_index][0] == NIL
            or program[toggle_index][0] == MUL
        ):
            raise NotImplementedError
        if len(program[toggle_index]) == 2:
            if program[toggle_index][0] == INC:
                program[toggle_index][0] = DEC
            else:
                program[toggle_index][0] = INC
        elif len(program[toggle_index]) == 3:
            if program[toggle_index][0] == JNZ:
                program[toggle_index][0] = CPY
            else:
                program[toggle_index][0] = JNZ
        else:
            raise NotImplementedError
        print(f"{program[toggle_index]}")
        simplify_program(program)
    return values, index + 1


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

    if changed:
        print(f"new_program = {program}")
        return simplify_program(program)


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
    values: Values = START_A, START_B, START_C, START_D
    index = 0
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
        elif current[0] == TGL:
            values, index = tgl(values, index, program)
        elif current[0] == NIL:
            values, index = nil(values, index, program)
        elif current[0] == ADD:
            values, index = add(values, index, program)
        elif current[0] == MUL:
            values, index = mul(values, index, program)
        else:
            raise NotImplementedError
        if 0 <= index < len(program):
            print(f"{index} {program[index]} {values}")
    print(program)
    print(values)
    print(f"a = {values[0]}")


if __name__ == "__main__":
    main()
