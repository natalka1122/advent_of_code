FILENAME, START = "demo.txt", "decab"  # expected abcde
FILENAME, START = "input.txt", "dbfgaehc"  # expected abcdefgh
# FILENAME, START = "input.txt", "fbgdceah"

SWAP = "swap"
ROTATE = "rotate"
REVERSE = "reverse"
MOVE = "move"
POSITION = "position"
LETTER = "letter"
LEFT = "left"
RIGHT = "right"
BASED = "based"


def formula(current, length) -> int:
    result = []
    if current < 9 and current % 2 == 1:
        old = (current - 1) // 2
        result.append(old)
    if current + length < 9 and (current + length) % 2 == 1:
        old = (current + length - 1) // 2
        result.append(old)
    if current >= 10 and current % 2 == 0:
        old = (current - 2) // 2
        result.append(old)
    if current + length >= 10 and (current + length) % 2 == 0:
        old = (current + length - 2) // 2
        result.append(old)
    if 10 <= current + 2 * length < 2 * length + 2 and current % 2 == 0:
        old = (current + 2 * length - 2) // 2
        result.append(old)
    if len(result) != 1:
        print(f"current = {current} length = {length} result = {result}")
        # raise NotImplementedError
    return result[0]


def main() -> None:
    lines = []
    result = START
    with open(FILENAME, "r") as file:
        for line_ in file:
            lines.append(line_.strip().split(" "))
    for line in lines[::-1]:
        if line[0] == SWAP:
            if line[1] == POSITION and line[4] == POSITION:
                min_pos, max_pos = sorted([int(line[2]), int(line[5])])
                result = (
                    result[:min_pos]
                    + result[max_pos]
                    + result[min_pos + 1 : max_pos]
                    + result[min_pos]
                    + result[max_pos + 1 :]
                )
            elif line[1] == LETTER and line[4] == LETTER:
                tmp = ""
                for letter in result:
                    if letter == line[2]:
                        tmp += line[5]
                    elif letter == line[5]:
                        tmp += line[2]
                    else:
                        tmp += letter
                result = tmp
            else:
                print(f"line = {line}")
                raise NotImplementedError
        elif line[0] == ROTATE:
            if line[1] == LEFT:
                index = int(line[2])
                result = result[-index:] + result[:-index]
            elif line[1] == RIGHT:
                index = int(line[2])
                result = result[index:] + result[:index]
            elif line[1] == BASED:
                index = result.index(line[6])
                # print(
                #     f"line = {line} index = {index} line[6] = {line[6]} result = {result}"
                # )
                new_index = formula(index, len(result))
                # index += 1
                # index = index % len(result)
                result = result[-new_index:] + result[:-new_index]
                # raise NotImplementedError
            else:
                raise NotImplementedError
        elif line[0] == REVERSE:
            min_pos, max_pos = sorted([int(line[2]), int(line[4])])
            result = (
                result[:min_pos]
                + result[min_pos : max_pos + 1][::-1]
                + result[max_pos + 1 :]
            )
        elif line[0] == MOVE:
            v1 = int(line[2])
            v2 = int(line[5])
            if v1 < v2:
                result = result[:v1] + result[v2] + result[v1:v2] + result[v2 + 1 :]
            elif v1 > v2:
                result = (
                    result[:v2]
                    + result[v2 + 1 : v1 + 1]
                    + result[v2]
                    + result[v1 + 1 :]
                )
            else:
                raise NotImplementedError
        else:
            print(f"line = {line}")
            raise NotImplementedError
        print(f"line = {line} result = {result}")
    print(result)


if __name__ == "__main__":
    main()
