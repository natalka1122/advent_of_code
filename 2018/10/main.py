import re
from PIL import Image

FILENAME = "demo.txt"
FILENAME = "input.txt"

STEPS = 1000000

def main():
    points = list()
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(
                r"position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>", line.strip()
            )
            if line_match is None:
                raise NotImplementedError
            x0, y0, dx, dy = map(int, line_match.groups())
            points.append((x0, y0, dx, dy))
    for step in range(STEPS):
        if step % 1000 == 0:
            print(step)
        min_y, max_y, min_x, max_x = points[0][0], points[0][0], points[0][1], points[0][1]
        for y, x, _, _ in points:
            min_y = min(min_y, y)
            min_x = min(min_x, x)
            max_y = max(max_y, y)
            max_x = max(max_x, x)
        if max_y-min_y < len(points) or max_x-min_x < len(points):
            print(step)
            img = Image.new("1", (max_y - min_y + 1, max_x - min_x + 1))
            data = img.load()
            for y, x, _, _ in points:
                print(y + min_y, x + min_x,"size=",(max_y - min_y + 1, max_x - min_x + 1))
                print(y,x)
                print(min_y, max_y, min_x, max_x)
                data[y - min_y, x - min_x] = 1
            img.save(f"image-{FILENAME.split('.')[0]}-{step}.png")
        for i in range(len(points)):
            points[i] = (
                points[i][0] + points[i][2],
                points[i][1] + points[i][3],
                points[i][2],
                points[i][3],
            )


if __name__ == "__main__":
    main()
