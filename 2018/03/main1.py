import re

FILENAME = "demo.txt"  # expected 4
FILENAME = "input.txt"


def main() -> None:
    claims = []
    with open(FILENAME, "r") as file:
        for line in file:
            line_match = re.match(r"#\d+ @ (\d+),(\d+): (\d+)x(\d+)", line.strip())
            if line_match is None:
                raise NotImplementedError
            claims.append(
                (
                    int(line_match.group(1)),
                    int(line_match.group(2)),
                    int(line_match.group(1)) + int(line_match.group(3)),
                    int(line_match.group(2)) + int(line_match.group(4)),
                )
            )
    print(claims)
    intersections = set()
    for i in range(len(claims) - 1):
        for j in range(i + 1, len(claims)):
            intersect = (
                (max(claims[i][0], claims[j][0]), min(claims[i][2], claims[j][2])),
                (max(claims[i][1], claims[j][1]), min(claims[i][3], claims[j][3])),
            )
            if intersect[0][0]==intersect[0][1] or intersect[1][0]==intersect[1][1]:
                continue
            for y in range(intersect[0][0],intersect[0][1]):
                for x in range(intersect[1][0],intersect[1][1]):
                    intersections.add((y,x))
    print(len(intersections))


if __name__ == "__main__":
    main()
