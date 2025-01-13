import re

FILENAME, TIME = "demo.txt", 1000  # expected 1120
FILENAME, TIME = "input.txt", 2503


def f(speed: int, time_fly: int, time_rest: int) -> int:
    rounds_count = TIME // (time_fly + time_rest)
    result = (speed * time_fly) * rounds_count
    time_left = TIME % (time_fly + time_rest)
    if time_left > time_fly:
        result += speed * time_fly
    else:
        result += speed * time_left
    return result


def main() -> None:
    best_distance = None
    with open(FILENAME, "r") as file:
        for line in file:
            reindeer_match = re.match(
                r"(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds\.",
                line.strip(),
            )
            if reindeer_match is None:
                raise NotImplementedError
            distance = f(
                int(reindeer_match.group(2)),
                int(reindeer_match.group(3)),
                int(reindeer_match.group(4)),
            )
            if best_distance is None or best_distance < distance:
                best_distance = distance
            print(reindeer_match.groups(), distance, best_distance)
    print(best_distance)


if __name__ == "__main__":
    main()
