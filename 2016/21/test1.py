MAX = 8


def f(current, length) -> int:
    result = []
    if current < 9 and current % 2 == 1:
        old = (current - 1) // 2
        if 0 <= old < length:
            result.append(old)
        else:
            print(f"1 old = {old} length = {length} current = {current}")
    if current + length < 9 and (current + length) % 2 == 1:
        old = (current + length - 1) // 2
        if 0 <= old < length:
            result.append(old)
        else:
            print(f"2 old = {old} length = {length} current = {current}")
    if 10 <= current and current % 2 == 0:
        old = (current - 2) // 2
        if 0 <= old < length:
            result.append(old)
        else:
            print(f"3 old = {old} length = {length} current = {current}")
    if 10 <= current + length and (current + length) % 2 == 0:
        old = (current + length - 2) // 2
        if 0 <= old < length:
            result.append(old)
        else:
            print(f"4 old = {old} length = {length} current = {current}")
    if 10 <= current + 2 * length < 2 * length + 2 and current % 2 == 0:
        old = (current + 2 * length - 2) // 2
        if 0 <= old < length:
            result.append(old)
        else:
            print(f"5 old = {old} length = {length} current = {current}")
    return result


def main():
    for length in range(1, MAX + 1):
        for old in range(length):
            if old < 4:
                current = 2 * old + 1
            else:
                current = 2 * old + 2
            case = f"{int(old<4)}{current//length}"
            current = current % length
            formula = f(current, length)
            result = old in formula
            if True:
                print(
                    f"old = {old} length = {length} current = {current} case = {case} formula = {formula} {result}"
                )
            if len(formula) == 0:
                raise NotImplementedError
            # if len(formula) > 1:
            #     print(
            #         f"old = {old} length = {length} current = {current} case = {case} formula = {formula} {result}"
            #     )
            if case == "11" and not result:
                raise NotImplementedError
            if case == "10" and not result:
                raise NotImplementedError
            if case == "00" and not result:
                raise NotImplementedError
            if case == "01" and not result:
                raise NotImplementedError
            if case == "02" and not result:
                raise NotImplementedError
            if not result:
                raise NotImplementedError


main()
