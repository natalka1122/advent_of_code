FILENAME = "demo.txt"  # expected 14897079
FILENAME = "input.txt"

BIG_NUMBER = 20201227
SUBJECT = 7


def transform(subject: int, value: int, cycles: int) -> int:
    result = value
    for _ in range(cycles):
        result = (result * subject) % BIG_NUMBER
    return result


def detransform(n: int) -> int:
    value = 1
    i = 0
    while True:
        value = transform(SUBJECT, value, 1)
        i += 1
        if value == n:
            return i


def main() -> None:
    with open(FILENAME, "r") as file:
        card_public_key = int(file.readline())
        door_public_key = int(file.readline())
    # print(f"card_public_key = {card_public_key}")
    # print(f"door_public_key = {door_public_key}")
    detransform_door_public_key = detransform(door_public_key)
    print(transform(subject=card_public_key, value=1, cycles=detransform_door_public_key))


if __name__ == "__main__":
    main()
