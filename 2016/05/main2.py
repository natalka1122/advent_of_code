import hashlib

# FILENAME = "demo.txt"  # expected 05ace8e3
FILENAME = "input.txt"
NONE = "_"


def md5(line: str, index: int) -> tuple[int, str] | None:
    result: str = hashlib.md5((line + str(index)).encode()).hexdigest()
    if "0" * 5 == result[:5] and "0" <= result[5] <= "7":
        return int(result[5]), result[6]
    return None


def main() -> None:
    result = NONE * 8
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            index = 0
            for _ in range(8):
                while True:
                    current = md5(line, index)
                    index += 1
                    if current is not None:
                        a, b = current
                        print(a, b)
                        if result[a] == NONE:
                            result = result[:a] + b + result[a + 1 :]
                            break
    print(result)


if __name__ == "__main__":
    main()
