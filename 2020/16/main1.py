import re

FILENAME = "demo1.txt"  # expected 71
FILENAME = "input.txt"


def merge(conditions: list[tuple[int, int]]) -> list[tuple[int, int]]:
    for i in range(1, len(conditions)):
        if conditions[i - 1][0] == conditions[i][0]:
            return merge(
                conditions[: i - 1]
                + [(conditions[i - 1][0], max(conditions[i - 1][1], conditions[i][1]))]
                + conditions[i + 1 :]
            )
        if conditions[i - 1][1] + 1 >= conditions[i][0]:
            return merge(
                conditions[: i - 1]
                + [(conditions[i - 1][0], max(conditions[i - 1][1], conditions[i][1]))]
                + conditions[i + 1 :]
            )
    return conditions


def main() -> None:
    result = 0
    is_conditions = True
    is_my_ticket = False
    is_nei_tickets = False
    conditions: list[tuple[int, int]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                if is_conditions:
                    is_conditions = False
                    is_my_ticket = True
                    print(conditions)
                    conditions = merge(sorted(conditions))
                    print(conditions)
                elif is_my_ticket:
                    is_my_ticket = False
                    is_nei_tickets = True
                else:
                    raise NotImplementedError
            elif is_conditions:
                current_match = re.match(r"[a-z ]+: (\d+)-(\d+) or (\d+)-(\d+)", line.strip())
                if current_match is None:
                    raise NotImplementedError
                conditions.append((int(current_match.group(1)), int(current_match.group(2))))
                conditions.append((int(current_match.group(3)), int(current_match.group(4))))
            elif is_my_ticket:
                pass
            elif is_nei_tickets:
                if ":" in line:
                    continue
                for number in map(int, line.split(",")):
                    is_valid = False
                    for c1, c2 in conditions:
                        if c1 <= number <= c2:
                            is_valid = True
                            break
                    if not is_valid:
                        result += number
            else:
                raise NotImplementedError
    print(result)


if __name__ == "__main__":
    main()
