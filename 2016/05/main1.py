import hashlib

FILENAME = "demo.txt"  # expected 18f47a30
FILENAME = "input.txt"


def md5(line: str, index: int) -> str | None:
    result: str = hashlib.md5((line + str(index)).encode()).hexdigest()
    if "0" * 5 == result[:5]:
        return result[5]
    return None


def main() -> None:
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            index = 0
            for _ in range(8):
                while True:
                    current = md5(line, index)
                    if current is not None:
                        index += 1
                        break
                    index += 1
                print(current, end="")
    print()


if __name__ == "__main__":
    main()
