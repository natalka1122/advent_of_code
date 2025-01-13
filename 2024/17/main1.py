from __future__ import annotations

# FILENAME = "demo_1.txt"  # expected 4,6,3,5,6,3,5,2,1,0
FILENAME = "input.txt"


def main():
    with open(FILENAME, "r") as file:
        register_a = int(file.readline().split(" ")[2])
        register_b = int(file.readline().split(" ")[2])
        register_c = int(file.readline().split(" ")[2])
        file.readline()
        program = list(map(int, file.readline().split(" ")[1].split(",")))
        for line in file:
            print(line)
    print(register_a, register_b, register_c, program)
    result = []
    pointer = 0
    while pointer < len(program) - 1:
        opcode = program[pointer]
        literal_op = program[pointer + 1]
        print(
            f"opcode = {opcode} literal_op = {literal_op} register_a = {register_a} register_b {register_b} register_c = {register_c}"
        )
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
            register_a = register_a // (2**combo_op)
        elif opcode == 1:
            register_b = register_b ^ literal_op
        elif opcode == 2:
            register_b = combo_op % 8
        elif opcode == 3:
            if register_a != 0:
                pointer = literal_op
                continue
        elif opcode == 4:
            register_b = register_b ^ register_c
        elif opcode == 5:
            result.append(combo_op % 8)
        elif opcode == 6:
            raise NotImplementedError
        elif opcode == 7:
            register_c = register_a // (2**combo_op)
        pointer += 2
    print(",".join(map(str, result)))


if __name__ == "__main__":
    main()
