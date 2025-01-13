FILENAME = "input.txt"


def f(a: int, b: int, c: int) -> bool:
    return a < b + c and b < a + c and c < a + b


def main() -> None:
    result = 0
    l1, l2, l3 = None, None, None
    with open(FILENAME, "r") as file:
        for line_ in file:
            line: list[int] = list(
                map(int, filter(lambda x: len(x.strip()) > 0, line_.split(" ")))
            )
            if l1 is None:
                l1 = line
            elif l2 is None:
                l2 = line
            elif l3 is None:
                l3 = line
                if f(l1[0], l2[0], l3[0]):
                    result += 1
                if f(l1[1], l2[1], l3[1]):
                    result += 1
                if f(l1[2], l2[2], l3[2]):
                    result += 1
                l1 = None
                l2 = None
                l3 = None
            else:
                raise NotImplementedError
    print(result)


if __name__ == "__main__":
    main()
