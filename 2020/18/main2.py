from collections.abc import Callable
import re

FILENAME = "demo.txt"
FILENAME = "input.txt"
FUNC: dict[str, Callable[[int, int], int]] = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}


def calc_rpn(rpn: list[str]) -> int:
    print(f"rpn = {rpn}")
    stack: list[int] = []
    for token in rpn:
        if token in FUNC:
            stack.append(FUNC[token](stack.pop(), stack.pop()))
        else:
            stack.append(int(token))
        # print(token, stack)
    print(stack)
    return stack[0]


def infix_to_rpn(line: list[str]) -> list[str]:
    stack: list[str] = []
    output = []
    for token in line:
        if token == "*":
            while len(stack) > 0 and stack[-1] in FUNC:
                output.append(stack.pop())
            stack.append(token)
        elif token == "+":
            while len(stack) > 0 and stack[-1] == "+":
                output.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            current = stack.pop()
            while current != "(":
                output.append(current)
                current = stack.pop()
        else:
            output.append(token)
    while len(stack) > 0:
        output.append(stack.pop())
    return output


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.findall(r"(\d+|\*|\+|\(|\))", line.strip())
            result += calc_rpn(infix_to_rpn(line_match))
    print(result)


if __name__ == "__main__":
    main()
