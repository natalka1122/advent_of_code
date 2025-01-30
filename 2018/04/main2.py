import re

FILENAME = "demo.txt"  # expected 4455
FILENAME = "input.txt"

SIXTY = 60


class Guard:
    def __init__(self, id: int):
        self.id = id
        self.sleep: list[tuple[tuple[int, int, int, int, int], tuple[int, int, int, int, int]]] = []
        self.total_time = 0
        self.intersect = {i: 0 for i in range(60)}
        self.sleepy_minute = 0
        self.sleepy_count = 0

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
        for t in range(t1[4], t2[4]):
            self.intersect[t] += 1
            if self.intersect[t] > self.sleepy_count:
                self.sleepy_minute = t
                self.sleepy_count = self.intersect[t]


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
    sleepy_guard = None
    sleepy_minute = 0
    sleepy_count = 0
    for guard_index, guard in guards.items():
        if guard.sleepy_count > sleepy_count:
            sleepy_count = guard.sleepy_count
            sleepy_minute = guard.sleepy_minute
            sleepy_guard = guard_index
    if sleepy_guard is None:
        raise NotImplementedError
    print(sleepy_guard, sleepy_minute)
    print(sleepy_guard * sleepy_minute)


if __name__ == "__main__":
    main()
