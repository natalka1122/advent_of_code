import hashlib

# FILENAME = "demo1_1.txt"  # expected 609043
# FILENAME = "demo1_2.txt"  # expected 1048970
FILENAME = "input.txt"


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for secret_key in file:
            while True:
                line = secret_key.strip() + str(result)
                if hashlib.md5(line.encode()).hexdigest().startswith("0" * 5):
                    break
                result += 1
    print(result)


if __name__ == "__main__":
    main()
