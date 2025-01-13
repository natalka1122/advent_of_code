import re

# FILENAME, WIDTH, HEIGHT = "demo.txt", 11, 7  # expected 12
FILENAME, WIDTH, HEIGHT = "input.txt", 101, 103
STEPS = 100


def main():
    q00, q01, q10, q11 = 0, 0, 0, 0
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"p=(-?\d+),(-?\d+)\sv=(-?\d+),(-?\d+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            x0, y0, dx, dy = map(int, line_match.groups())
            # print(x0, y0, dx, dy)
            x = (x0 + dx * STEPS) % WIDTH
            y = (y0 + dy * STEPS) % HEIGHT
            # print(x, y)
            if x < WIDTH // 2 and y < HEIGHT // 2:
                q00 += 1
            elif x < WIDTH // 2 and y > HEIGHT // 2:
                q10 += 1
            elif x > WIDTH // 2 and y < HEIGHT // 2:
                q01 += 1
            elif x > WIDTH // 2 and y > HEIGHT // 2:
                q11 += 1
    print(q00, q01, q10, q11)
    print(q00 * q01 * q10 * q11)


if __name__ == "__main__":
    main()
