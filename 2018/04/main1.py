import re

FILENAME = "demo.txt"  # expected 240
FILENAME = "input.txt"

SIXTY = 60


class Guard:
    def __init__(self, id: int):
        self.id = id
        self.sleep: list[tuple[tuple[int, int, int, int, int], tuple[int, int, int, int, int]]] = []
        self.total_time = 0

    def add(self, t1: tuple[int, int, int, int, int], t2: tuple[int, int, int, int, int]) -> None:
        self.sleep.append((t1, t2))
        if t1[0] != t2[0]:
            raise NotImplementedError
        if t1[1] != t2[1]:
            raise NotImplementedError
        if t1[2] != t2[2]:
            raise NotImplementedError
        if t1[3] != t2[3]:
            raise NotImplementedError
        self.total_time += t2[4] - t1[4]


def main() -> None:
    timesheet = set()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (wakes up|falls asleep|Guard #(\d+) begins shift)",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            timesheet.add(line_match.groups())
    guards: dict[int, Guard] = dict()
    start_time: tuple[int, int, int, int, int] | None = None
    current_guard_index: int | None = None
    sleepy_index = None
    sleepy_time = 0
    for yy, mm, dd, hh, ss, text, number in sorted(timesheet):
        if number is None:
            if current_guard_index is None:
                raise NotImplementedError
            timestamp = int(yy), int(mm), int(dd), int(hh), int(ss)
            if text == "falls asleep":
                if start_time is not None:
                    raise NotImplementedError
                start_time = timestamp
            elif text == "wakes up":
                if start_time is None:
                    raise NotImplementedError
                guards[current_guard_index].add(start_time, timestamp)
                start_time = None
                if guards[current_guard_index].total_time > sleepy_time:
                    sleepy_time = guards[current_guard_index].total_time
                    sleepy_index = current_guard_index
            else:
                raise NotImplementedError
        elif isinstance(number, str):
            if start_time is not None:
                raise NotImplementedError
            current_guard_index = int(number)
            if current_guard_index not in guards:
                guards[current_guard_index] = Guard(current_guard_index)
        else:
            raise NotImplementedError
    if sleepy_index is None:
        raise NotImplementedError
    intersect = {i: 0 for i in range(60)}
    sleepy_minute = 0
    for i in range(len(guards[sleepy_index].sleep)):
        mm0 = guards[sleepy_index].sleep[i][0][4]
        mm1 = guards[sleepy_index].sleep[i][1][4]
        for t in range(mm0, mm1):
            intersect[t] += 1
            if intersect[t] > intersect[sleepy_minute]:
                sleepy_minute = t
    print(sleepy_minute * sleepy_index)


if __name__ == "__main__":
    main()
