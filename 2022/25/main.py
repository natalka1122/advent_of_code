FILENAME = "demo.txt"  # expected 2=-1=0
FILENAME = "input.txt"


def snafu_to_int(snafu: str) -> int:
    result = 0
    for symbol in snafu:
        if symbol == "2":
            result = result * 5 + 2
        elif symbol == "1":
            result = result * 5 + 1
        elif symbol == "0":
            result = result * 5
        elif symbol == "-":
            result = result * 5 - 1
        elif symbol == "=":
            result = result * 5 - 2
        else:
            print(f"symbol = {symbol}")
            raise NotImplementedError
    print(f"snafu = {snafu} result = {result}")
    return result


def int_to_snafu(num:int) -> str:
    if num == 0:
        return ""
    if num % 5 == 0:
        return int_to_snafu(num // 5) + "0"
    if num % 5 == 1:
        return int_to_snafu(num // 5) + "1"
    if num % 5 == 2:
        return int_to_snafu(num // 5) + "2"
    if num % 5 == 3:
        return int_to_snafu((num + 2) // 5) + "="
    if num % 5 == 4:
        return int_to_snafu((num + 1) // 5) + "-"
    raise NotImplementedError


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += snafu_to_int(line.strip())
    print(int_to_snafu(result))


if __name__ == "__main__":
    main()
