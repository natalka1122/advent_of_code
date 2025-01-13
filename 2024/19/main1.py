import functools

# FILENAME = "demo.txt"  # expected 6
FILENAME = "input.txt"


@functools.cache
def f(design, patterns):
    if not design:
        # print(True)
        return True
    # print(f"design = {design} patterns = {patterns}")
    for pattern in patterns:
        if design.startswith(pattern) and f(design[len(pattern) :], patterns):
            return True
    # print(False)
    return False


def main():
    result = 0
    with open(FILENAME, "r") as file:
        patterns = tuple(file.readline().strip().split(", "))
        file.readline()
        i = 0
        for line in file:
            i += 1
            print(i, line)
            if f(line.strip(), patterns):
                result += 1
    print(result)


if __name__ == "__main__":
    main()
