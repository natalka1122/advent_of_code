import hashlib

FILENAME = "input.txt"


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for secret_key in file:
            while True:
                line = secret_key.strip() + str(result)
                if hashlib.md5(line.encode()).hexdigest().startswith("0" * 6):
                    break
                result += 1
    print(result)


if __name__ == "__main__":
    main()
