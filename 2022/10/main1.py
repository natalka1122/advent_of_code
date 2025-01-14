FILENAME = "demo1.txt"
FILENAME = "demo2.txt"  # expected 13140
FILENAME = "input.txt"

TARGET_STEPS = [20, 60, 100, 140, 180, 220]


def main() -> None:
    result = 0
    step = 1
    x = 1
    with open(FILENAME, "r") as file:
        for line_ in file:
            line = line_.strip()
            if line == "noop":
                step += 1
                if step in TARGET_STEPS:
                    result += step * x
                    print(step, x, "CASE1")
                continue
            if line.startswith("addx "):
                step += 1
                if step in TARGET_STEPS:
                    result += step * x
                    print(step, x, "CASE2")
                step += 1
                x += int(line.split(" ")[1])
                if step in TARGET_STEPS:
                    result += step * x
                    print(step, x, "CASE3")

    print(result)


if __name__ == "__main__":
    main()
