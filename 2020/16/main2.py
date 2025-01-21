import re

FILENAME, FIELD_START = "demo2.txt", "class"  # expected 12
FILENAME, FIELD_START = "demo2.txt", "row"  # expected 11
FILENAME, FIELD_START = "demo2.txt", "seat"  # expected 13
FILENAME, FIELD_START = "input.txt", "departure"


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
    conditions: dict[str, list[tuple[int, int]]] = dict()
    conditions_set: list[tuple[int, int]] = []
    my_ticket: tuple[int, ...] | None = None
    nei_tickets: list[tuple[int, ...]] = []
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                if is_conditions:
                    is_conditions = False
                    is_my_ticket = True
                    if conditions_set is None:
                        raise NotImplementedError
                    # print(conditions_set)
                    conditions_set = merge(sorted(conditions_set))
                    # print(conditions_set)
                elif is_my_ticket:
                    is_my_ticket = False
                    is_nei_tickets = True
                else:
                    raise NotImplementedError
            elif is_conditions:
                current_match = re.match(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", line.strip())
                if current_match is None:
                    raise NotImplementedError
                conditions[current_match.group(1)] = [
                    (int(current_match.group(2)), int(current_match.group(3))),
                    (int(current_match.group(4)), int(current_match.group(5))),
                ]
                conditions_set.extend(conditions[current_match.group(1)])
            elif is_my_ticket:
                if ":" in line:
                    continue
                if my_ticket is not None:
                    raise NotImplementedError
                my_ticket = tuple(map(int, line.split(",")))
            elif is_nei_tickets:
                if ":" in line:
                    continue
                for number in map(int, line.split(",")):
                    is_valid = False
                    for c1, c2 in conditions_set:
                        if c1 <= number <= c2:
                            is_valid = True
                            break
                    if not is_valid:
                        break
                if not is_valid:
                    continue
                nei_tickets.append(tuple(map(int, line.split(","))))

            else:
                raise NotImplementedError
    if my_ticket is None:
        raise NotImplementedError
    print(f"nei_tickets = {nei_tickets}")
    print(f"conditions = {conditions}")
    ticket_fields_set: list[set[str]] = []
    for index in range(len(nei_tickets[0])):
        ticket_fields_set.append(set())
        for field in conditions:
            is_valid = True
            for ticket in nei_tickets:
                if (
                    not conditions[field][0][0] <= ticket[index] <= conditions[field][0][1]
                    and not conditions[field][1][0] <= ticket[index] <= conditions[field][1][1]
                ):
                    is_valid = False
                    break
            if is_valid:
                ticket_fields_set[-1].add(field)
    print(f"ticket_fields_set = {ticket_fields_set}")
    is_changed = True
    while is_changed:
        is_changed = False
        for index0 in range(len(ticket_fields_set)):
            if len(ticket_fields_set[index0]) == 1:
                for value0 in ticket_fields_set[index0]:
                    for index1 in range(len(ticket_fields_set)):
                        if index0 == index1:
                            continue
                        if value0 in ticket_fields_set[index1]:
                            ticket_fields_set[index1].remove(value0)
                            is_changed = True
                            break
    print(f"ticket_fields_set = {ticket_fields_set}")
    ticket_fields: list[str] = []
    for index in range(len(ticket_fields_set)):
        if len(ticket_fields_set[index]) != 1:
            raise NotImplementedError
        for value in ticket_fields_set[index]:
            ticket_fields.append(value)
    print(f"ticket_fields = {ticket_fields}")
    result = 1
    for index in range(len(my_ticket)):
        if ticket_fields[index].startswith(FIELD_START):
            result *= my_ticket[index]
    print(result)


if __name__ == "__main__":
    main()
