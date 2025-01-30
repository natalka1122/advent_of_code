import re

FILENAME = "demo.txt"  # expected 3
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
    # print(claims)
    for i in range(len(claims)):
        no_intersections = True
        for j in range(len(claims)):
            if i == j:
                continue
            intersect = (
                (max(claims[i][0], claims[j][0]), min(claims[i][2], claims[j][2])),
                (max(claims[i][1], claims[j][1]), min(claims[i][3], claims[j][3])),
            )
            if intersect[0][0] < intersect[0][1] and intersect[1][0] < intersect[1][1]:
                no_intersections = False
                break
        if no_intersections:
            print(i + 1)
            return


if __name__ == "__main__":
    main()
