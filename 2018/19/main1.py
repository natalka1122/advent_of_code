from __future__ import annotations
from collections.abc import Callable

FILENAME = "demo.txt"
FILENAME = "input.txt"

Triple = tuple[int, int, int]
Sixtuple = tuple[int, int, int, int, int, int]


def addr(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = values[instruction[0]] + values[instruction[1]]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def addi(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = values[instruction[0]] + instruction[1]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def mulr(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = values[instruction[0]] * values[instruction[1]]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def muli(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = values[instruction[0]] * instruction[1]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def banr(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = values[instruction[0]] & values[instruction[1]]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def bani(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = values[instruction[0]] & instruction[1]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def borr(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = values[instruction[0]] | values[instruction[1]]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def bori(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = values[instruction[0]] | instruction[1]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def setr(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = values[instruction[0]]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def seti(values: Sixtuple, instruction: Triple) -> Sixtuple:
    value = instruction[0]
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def gtir(values: Sixtuple, instruction: Triple) -> Sixtuple:
    if instruction[0] > values[instruction[1]]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def gtri(values: Sixtuple, instruction: Triple) -> Sixtuple:
    if values[instruction[0]] > instruction[1]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def gtrr(values: Sixtuple, instruction: Triple) -> Sixtuple:
    if values[instruction[0]] > values[instruction[1]]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def eqir(values: Sixtuple, instruction: Triple) -> Sixtuple:
    if instruction[0] == values[instruction[1]]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def eqri(values: Sixtuple, instruction: Triple) -> Sixtuple:
    if values[instruction[0]] == instruction[1]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


def eqrr(values: Sixtuple, instruction: Triple) -> Sixtuple:
    if values[instruction[0]] == values[instruction[1]]:
        value = 1
    else:
        value = 0
    result: tuple[int, ...] = values[: instruction[2]] + (value,) + values[instruction[2] + 1 :]
    if len(result) != 6:
        raise NotImplementedError
    return result


OPERATIONS: dict[str, Callable[[Sixtuple, Triple], Sixtuple]] = {
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


def main() -> None:
    ipointer: int | None = None
    program: list[tuple[Callable[[Sixtuple, Triple], Sixtuple], tuple[int, int, int]]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            if line.startswith("#ip"):
                ipointer = int(line.split(" ")[1])
            else:
                line_split = line.split(" ")
                program.append(
                    (
                        OPERATIONS[line_split[0]],
                        (int(line_split[1]), int(line_split[2]), int(line_split[3])),
                    )
                )
    if ipointer is None:
        raise
    register: Sixtuple = (0, 0, 0, 0, 0, 0)
    while 0 <= register[ipointer] < len(program):
        pointer = register[ipointer]
        register = program[pointer][0](register, program[pointer][1])
        # print(register)
        if register[ipointer] < 0 or register[ipointer] >= len(program):
            break
        register = addi(register, (ipointer, 1, ipointer))
    print(register[0])


if __name__ == "__main__":
    main()
