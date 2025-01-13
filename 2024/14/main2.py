import re
from PIL import Image

FILENAME, WIDTH, HEIGHT = "input.txt", 101, 103
STEPS = 10000


def main():
    robots = list()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"p=(-?\d+),(-?\d+)\sv=(-?\d+),(-?\d+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            x0, y0, dx, dy = map(int, line_match.groups())
            robots.append((x0, y0, dx, dy))
            x = (x0 + dx * STEPS) % WIDTH
            y = (y0 + dy * STEPS) % HEIGHT
    for step in range(STEPS):
        img = Image.new("1", (WIDTH, HEIGHT))
        data = img.load()
        for robot in robots:
            x0, y0, dx, dy = robot
            x = (x0 + dx * step) % WIDTH
            y = (y0 + dy * step) % HEIGHT
            data[x, y] = 1
        img.save(f"image{step}.png")


if __name__ == "__main__":
    main()
