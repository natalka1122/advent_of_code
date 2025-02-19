import math

# FILENAME = "demo.txt"
FILENAME = "input.txt"


def main():
    with open(FILENAME, "r") as file:
        race_time = int("".join(x for x in file.readline().split() if x.isdigit()))
        race_distance = int("".join(x for x in file.readline().split() if x.isdigit()))
    print(race_time, race_distance)
    b = race_distance
    p = race_time
    x1 = math.ceil((p - math.sqrt(p * p - 4 * b)) / 2)
    if x1 * (p - x1) == b:
        x1 += 1
    x2 = math.floor((p + math.sqrt(p * p - 4 * b)) / 2)
    if x2 * (p - x2) == b:
        x2 -= 1
    result = x2 - x1 + 1
    print(f"x1 = {x1} x2 = {x2}, x2-x1 = {x2-x1}")
    print(result)


if __name__ == "__main__":
    main()
