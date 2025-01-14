from __future__ import annotations
from collections.abc import Iterator
from functools import cmp_to_key

FILENAME = "demo.txt"  # expected 13
FILENAME = "input.txt"

DIVIDER = ["[[2]]", "[[6]]"]


def get_item(line: str) -> Iterator[str]:
    if line[0] != "[" or line[-1] != "]":
        raise NotImplementedError
    stack: int = 0
    current: str = ""
    for symbol in line:
        if symbol == "[":
            stack += 1
            if stack != 1:
                current += symbol
        elif symbol == "]":
            if stack == 1 and len(current) > 0:
                yield current
            else:
                current += symbol
            stack -= 1
        elif symbol == ",":
            if stack == 1:
                yield current
                current = ""
            else:
                current += symbol
        else:
            current += symbol


def eq(line1: str, line2: str) -> bool:
    # print(f"eq: {line1} {line2}")
    if line1[0] == "[" and line2[0] == "[":
        line1_iter = get_item(line1)
        line2_iter = get_item(line2)
        is_ending = False
        try:
            item1 = next(line1_iter)
        except StopIteration:
            is_ending = True
        try:
            item2 = next(line2_iter)
        except StopIteration:
            if is_ending:
                # print(f"eq: {line1} {line2} -> True", "case eq:01")
                return True
            else:
                # print(f"eq: {line1} {line2} -> False", "case eq:02")
                return False
        if is_ending:
            # print(f"eq: {line1} {line2} -> False", "case eq:03")
            return False
        while eq(item1, item2):
            try:
                item1 = next(line1_iter)
            except StopIteration:
                is_ending = True
            try:
                item2 = next(line2_iter)
            except StopIteration:
                if is_ending:
                    # print(f"eq: {line1} {line2} -> True", "case eq:11")
                    return True
                else:
                    # print(f"eq: {line1} {line2} -> False", "case eq:12")
                    return False
            if is_ending:
                # print(f"eq: {line1} {line2} -> False", "case eq:13")
                return False
        # print(f"eq: {line1} {line2} -> False", "case eq:21")
        return False
    elif line1.isdigit() and line2.isdigit():
        # print(f"eq: {line1} {line2} -> {int(line1) == int(line2)}", "case eq:31")
        return int(line1) == int(line2)
    elif line1[0] == "[" and line2.isdigit():
        result = eq(line1, f"[{line2}]")
        # print(f"eq: {line1} {line2} -> {result}", "case eq:41")
        return result
    elif line1.isdigit() and line2[0] == "[":
        result = eq(f"[{line1}]", line2)
        # print(f"eq: {line1} {line2} -> {result}", "case eq:42")
        return result
    raise NotImplementedError


def lt(line1: str, line2: str) -> bool:
    # print(f"lt: {line1} {line2}")
    if line1[0] == "[" and line2[0] == "[":
        line1_iter = get_item(line1)
        line2_iter = get_item(line2)
        is_ending = False
        try:
            item1 = next(line1_iter)
        except StopIteration:
            is_ending = True
        try:
            item2 = next(line2_iter)
        except StopIteration:
            if is_ending:
                print(f"lt: {line1} {line2} -> False", "case lt:01")
                raise NotImplementedError
                return False
            else:
                # print(f"lt: {line1} {line2} -> False", "case lt:02")
                return False
        if is_ending:
            # print(f"lt: {line1} {line2} -> True", "case lt:03")
            return True
        while eq(item1, item2):
            try:
                item1 = next(line1_iter)
            except StopIteration:
                is_ending = True
            try:
                item2 = next(line2_iter)
            except StopIteration:
                if is_ending:
                    # print(f"lt: {line1} {line2} -> False", "case lt:11")
                    raise NotImplementedError
                    return False
                else:
                    # print(f"lt: {line1} {line2} -> False", "case lt:12")
                    return False
            if is_ending:
                # print(f"lt: {line1} {line2} -> True", "case lt:13")
                return True
        if lt(item1, item2):
            # print(f"lt: {line1} {line2} -> True", "case lt:21")
            return True
        elif eq(item1, item2):
            raise NotImplementedError
        else:
            # print(f"lt: {line1} {line2} -> False", "case lt:22")
            return False
    elif line1.isdigit() and line2.isdigit():
        # print(f"lt: {line1} {line2} -> {int(line1) < int(line2)}", "case lt:31")
        return int(line1) < int(line2)
    elif line1[0] == "[" and line2.isdigit():
        result = lt(line1, f"[{line2}]")
        # print(f"lt: {line1} {line2} -> {result}", "case lt:41")
        return result
    elif line1.isdigit() and line2[0] == "[":
        result = lt(f"[{line1}]", line2)
        # print(f"lt: {line1} {line2} -> {result}", "case lt:42")
        return result
    raise NotImplementedError


def compare(item1: str, item2: str) -> int:
    if eq(item1, item2):
        return 0
    if lt(item1, item2):
        return -1
    return 1


def main() -> None:
    lines = DIVIDER.copy()
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) != 0:
                lines.append(line)
    lines.sort(key=cmp_to_key(compare))
    print(lines)
    result = 1
    for i in range(len(lines)):
        if lines[i] in DIVIDER:
            result *= i + 1
    print(result)


if __name__ == "__main__":
    main()
