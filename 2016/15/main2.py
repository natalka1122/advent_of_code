import re

FILENAME = "demo.txt"  # expected 5
FILENAME = "input.txt"


def main() -> None:
    disks = dict()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).",
                line.strip(),
            )
            if line_match is None:
                raise NotImplementedError
            disks[int(line_match.group(1))] = tuple(map(int, line_match.groups()[1:]))
    max_disk_number = max(disks.keys())
    disks[max_disk_number + 1] = (11, 0)
    print(disks)
    t = 0
    found = False
    while not found:
        found = True
        for key, value in disks.items():
            length, start = value
            if (key + t + start) % length != 0:
                found = False
                break
        t += 1
    print(f"t = {t-1}")


if __name__ == "__main__":
    main()
