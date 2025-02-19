from __future__ import annotations
from collections.abc import Iterator

FILENAME = "demo.txt"  # expected 13
FILENAME = "input.txt"


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
    print(f"eq: {line1} {line2}")
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
                print(f"eq: {line1} {line2} -> True", "case eq:01")
                return True
            else:
                print(f"eq: {line1} {line2} -> False", "case eq:02")
                return False
        if is_ending:
            print(f"eq: {line1} {line2} -> False", "case eq:03")
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
                    print(f"eq: {line1} {line2} -> True", "case eq:11")
                    return True
                else:
                    print(f"eq: {line1} {line2} -> False", "case eq:12")
                    return False
            if is_ending:
                print(f"eq: {line1} {line2} -> False", "case eq:13")
                return False
        print(f"eq: {line1} {line2} -> False", "case eq:21")
        return False
    elif line1.isdigit() and line2.isdigit():
        print(f"eq: {line1} {line2} -> {int(line1) == int(line2)}", "case eq:31")
        return int(line1) == int(line2)
    elif line1[0] == "[" and line2.isdigit():
        result = eq(line1, f"[{line2}]")
        print(f"eq: {line1} {line2} -> {result}", "case eq:41")
        return result
    elif line1.isdigit() and line2[0] == "[":
        result = eq(f"[{line1}]", line2)
        print(f"eq: {line1} {line2} -> {result}", "case eq:42")
        return result
    raise NotImplementedError


def lt(line1: str, line2: str) -> bool:
    print(f"lt: {line1} {line2}")
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
                print(f"lt: {line1} {line2} -> False", "case lt:02")
                return False
        if is_ending:
            print(f"lt: {line1} {line2} -> True", "case lt:03")
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
                    print(f"lt: {line1} {line2} -> False", "case lt:11")
                    raise NotImplementedError
                    return False
                else:
                    print(f"lt: {line1} {line2} -> False", "case lt:12")
                    return False
            if is_ending:
                print(f"lt: {line1} {line2} -> True", "case lt:13")
                return True
        if lt(item1, item2):
            print(f"lt: {line1} {line2} -> True", "case lt:21")
            return True
        elif eq(item1, item2):
            raise NotImplementedError
        else:
            print(f"lt: {line1} {line2} -> False", "case lt:22")
            return False
    elif line1.isdigit() and line2.isdigit():
        print(f"lt: {line1} {line2} -> {int(line1) < int(line2)}", "case lt:31")
        return int(line1) < int(line2)
    elif line1[0] == "[" and line2.isdigit():
        result = lt(line1, f"[{line2}]")
        print(f"lt: {line1} {line2} -> {result}", "case lt:41")
        return result
    elif line1.isdigit() and line2[0] == "[":
        result = lt(f"[{line1}]", line2)
        print(f"lt: {line1} {line2} -> {result}", "case lt:42")
        return result
    raise NotImplementedError


def main() -> None:
    index = 1
    result = 0
    line1 = None
    line2 = None
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if len(line) == 0:
                if line is None or line2 is None:
                    raise NotImplementedError
                if lt(line1, line2):
                    print(index)
                    result += index
                line1 = None
                line2 = None
                index += 1
                print(f"=== {index} ===")
            elif line1 is None and line2 is None:
                line1 = line
            elif line1 is not None and line2 is None:
                line2 = line
            else:
                raise NotImplementedError
    if line1 is None or line2 is None:
        raise NotImplementedError
    if lt(line1, line2):
        print(index)
        result += index
    print(result)


if __name__ == "__main__":
    main()
