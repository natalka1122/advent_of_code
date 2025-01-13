import functools
from hashlib import md5
import re

FILENAME = "demo.txt"  # expected 22859
FILENAME = "input.txt"
SIXTY_FOUR = 64
THOUSAND = 1000
FIVE = 5
COUNT = 2016


@functools.cache
def get_extended_hash(line: str, index: int) -> str:
    result = md5((line + str(index)).encode()).hexdigest()
    for _ in range(COUNT):
        result = md5(result.encode()).hexdigest()
    return result


def f(line: str) -> int:
    index = 0
    for i in range(SIXTY_FOUR):
        next_condition = False
        while not next_condition:
            index += 1
            hash_match = re.search(r"(.)\1\1", get_extended_hash(line, index))
            if hash_match is None:
                continue
            target_line = hash_match.group(1) * FIVE
            # print(f"index = {index} target_line = {target_line}")
            for j in range(THOUSAND):
                if target_line in get_extended_hash(line, index + 1 + j):
                    next_condition = True
                    print(f"good: index = {index} j = {j}")
        print(f"i = {i} index = {index}")

    return index


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            print(f(line.strip()))


if __name__ == "__main__":
    main()
