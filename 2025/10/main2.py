from z3 import Int, Optimize, sat

# FILENAME = "demo.txt"  # expected 33
FILENAME = "input.txt"


int_tuple = tuple[int, ...]


def f(targets: int_tuple, togglers: list[int_tuple]) -> int:
    equations: list[list[int]] = []
    for i in range(len(targets)):
        equations.append([])
        for toggler in togglers:
            if i in toggler:
                equations[i].append(1)
            else:
                equations[i].append(0)

    xs = [Int(f"x{i+1}") for i in range(len(togglers))]
    opt = Optimize()
    for index, eq in enumerate(equations):
        coeffs = eq
        b = targets[index]
        opt.add(sum(coeffs[i] * xs[i] for i in range(len(togglers))) == b)
    for x in xs:
        opt.add(x >= 0)
    opt.minimize(sum(xs))

    res = opt.check()
    if res == sat:
        m = opt.model()
        result = sum([m[x].as_long() for x in xs])
        return result
    print("No solution:", res)
    raise NotImplementedError


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip().split(" ")
            target = tuple(map(int, line[-1][1:-1].split(",")))
            togglers = list(map(lambda x: tuple(map(int, x[1:-1].split(","))), line[1:-1]))
            result += f(target, togglers)

    print(result)


if __name__ == "__main__":
    main()
