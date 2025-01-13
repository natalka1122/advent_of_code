MAX = 20


def rotate_left(x: int, line: str) -> str:
    x = x % len(line)
    return line[x:] + line[:x]


def rotate_right(x: int, line: str) -> str:
    return rotate_left(-x, line)


def rotate_based(x: str, line: str) -> str:
    if line.count(x) != 1:
        raise NotImplementedError
    index = line.index(x)
    if index < 4:
        shift = index + 1
    else:
        shift = index + 2
    return rotate_right(shift, line)


def f(current, length) -> int:
    result = []
    if current % 2 == 1 and 1 <= current < 9:
        shift = (current + 1) // 2
        result.append("case 10")
        result.append(shift)
    if (current + length) % 2 == 1 and 1 <= current + length < 9:
        shift = (current + length + 1) // 2
        result.append("case 11")
        result.append(shift)
    if current % 2 == 0 and current >= 10:
        shift = current // 2 + 1
        result.append("case 00")
        result.append(shift)
    if (current + length) % 2 == 0 and current + length >= 10:
        shift = (current + length) // 2 + 1
        result.append("case 01")
        result.append(shift)
    if current % 2 == 0 and current + 2 * length >= 10:
        shift = (current + 2 * length) // 2 + 1
        result.append("case 02")
        result.append(shift)
    print(f"current = {current} length = {length} shift = {result}")
    return result


def unrotate_based(x: str, line: str) -> str:
    shift = f(line.index(x), len(line))
    return list(
        map(
            lambda x: rotate_left(x[1], line) if x[0] % 2 == 1 else x[1],
            enumerate(shift),
        )
    )


def main():
    for length in range(1, MAX + 1):
        line = "".join([chr(i) for i in range(ord("a"), ord("a") + length)])
        for index in range(length):
            symbol = line[index]
            rotated_line = rotate_based(symbol, line)
            final_line = unrotate_based(symbol, rotated_line)
            print(
                f"index = {index} line = {line} rotated_line = {rotated_line} final_line = {final_line}"
            )
            for l in final_line[1::2]:
                if rotate_based(symbol, l) != rotated_line:
                    print(f"this does not work: {l}")
                    raise NotImplementedError


main()
