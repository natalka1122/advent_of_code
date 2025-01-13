import re

# FILENAME, TIME_LIMIT = "demo.txt", 1000  # expected 689
FILENAME, TIME_LIMIT = "input.txt", 2503


def f(speed: int, time_fly: int, time_rest: int, time_limit: int) -> int:
    rounds_count = time_limit // (time_fly + time_rest)
    result = (speed * time_fly) * rounds_count
    time_left = time_limit % (time_fly + time_rest)
    if time_left > time_fly:
        result += speed * time_fly
    else:
        result += speed * time_left
    return result


def main() -> None:
    reindeers: dict[str, tuple[int, int, int]] = dict()
    dist: dict[str, int] = dict()
    score: dict[str, int] = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            reindeer_match = re.match(
                r"(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+) seconds\.",
                line.strip(),
            )
            if reindeer_match is None:
                raise NotImplementedError
            name = reindeer_match.group(1)
            reindeers[name] = (
                int(reindeer_match.group(2)),
                int(reindeer_match.group(3)),
                int(reindeer_match.group(4)),
            )
            score[name] = 0
            dist[name] = 0
    print(reindeers)
    for time in range(TIME_LIMIT):
        best_dist = None
        for reindeer in reindeers:
            dist[reindeer] = f(
                reindeers[reindeer][0],
                reindeers[reindeer][1],
                reindeers[reindeer][2],
                time + 1,
            )
            if best_dist is None or dist[reindeer] > best_dist:
                best_dist = dist[reindeer]
        for reindeer in reindeers:
            if dist[reindeer] == best_dist:
                score[reindeer] += 1
    print(score)
    print(max(score.values()))


if __name__ == "__main__":
    main()
