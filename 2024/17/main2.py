from __future__ import annotations

# FILENAME = "demo_2.txt"  # expected 117440
FILENAME = "input.txt"


def f(register_a: int, program: tuple[int, ...]) -> str:
    register_b = 0
    register_c = 0
    pointer = 0
    result = []
    while pointer < len(program) - 1:
        opcode = program[pointer]
        literal_op = program[pointer + 1]
        if 0 <= literal_op <= 3:
            combo_op = literal_op
        elif literal_op == 4:
            combo_op = register_a
        elif literal_op == 5:
            combo_op = register_b
        elif literal_op == 6:
            combo_op = register_c
        else:
            combo_op = None
        if opcode == 0:
            if combo_op is None:
                raise NotImplementedError
            register_a = register_a // (2**combo_op)
        elif opcode == 1:
            register_b = register_b ^ literal_op
        elif opcode == 2:
            if combo_op is None:
                raise NotImplementedError
            register_b = combo_op % 8
        elif opcode == 3:
            if register_a != 0:
                pointer = literal_op
                continue
        elif opcode == 4:
            register_b = register_b ^ register_c
        elif opcode == 5:
            if combo_op is None:
                raise NotImplementedError
            result.append(combo_op % 8)
        elif opcode == 6:
            if combo_op is None:
                raise NotImplementedError
            register_b = register_a // (2**combo_op)
        elif opcode == 7:
            if combo_op is None:
                raise NotImplementedError
            register_c = register_a // (2**combo_op)
        pointer += 2
    return "".join(map(str, result))


def main() -> None:
    with open(FILENAME, "r") as file:
        for _ in range(4):
            file.readline()
        program = tuple(map(int, file.readline().split(" ")[1].split(",")))
        for line in file:
            print(line)
    program_str = "".join(map(str, program))
    result = []
    index = 0
    start_num = 0
    while index < len(program):
        found_flag = False
        for num in range(start_num, 8):
            result.append(num)
            number = int("".join(map(str, result)), 8)
            print(
                f"number = {number} oct(number) = {oct(number)} result = {result} program_str[-index-1:] = {program_str[-index-1:]}, f(number, program) = {f(number, program)}"
            )
            if program_str[-index - 1 :] == f(number, program):
                print(f"found: index = {index}, num = {num}")
                found_flag = True
                break
            else:
                result.pop()
        if not found_flag:
            start_num = result.pop() + 1
            index -= 1
        else:
            start_num = 0
            index += 1
    print(number)


if __name__ == "__main__":
    main()
