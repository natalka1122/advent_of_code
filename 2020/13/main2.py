FILENAME = "demo.txt"  # expected 1068781
FILENAME = "input.txt"


def gcdExtended(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def chinese_remainder_theorem(n1: int, a1: int, n2: int, a2: int) -> int:
    gcd, m1, m2 = gcdExtended(n1, n2)
    if abs(gcd) != 1:
        print(f"n1 = {n1}", f"n2 = {n2}", f"gcd = {gcd}", f"m1 = {m1}", f"m2 = {m2}")
        raise NotImplementedError
    return a1 * m2 * n2 + a2 * m1 * n1


def main() -> None:
    timestamp = None
    buses: list[int] = []
    with open(FILENAME, "r") as file:
        for line in file:
            if timestamp is None:
                timestamp = int(line)
            else:
                buses = list(
                    map(lambda x: int(x) if x.isdigit() else None, line.strip().split(","))
                )
    if timestamp is None:
        raise NotImplementedError
    print(buses)
    number1 = None
    reminder1 = None
    for index, num in enumerate(buses):
        if num is None:
            continue
        if number1 is None:
            number1 = num
            reminder1 = -index
        else:
            reminder1 = chinese_remainder_theorem(number1, reminder1, num, -index)
            number1 *= num
            reminder1 = reminder1 % number1
    print(reminder1)


if __name__ == "__main__":
    main()
