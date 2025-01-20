FILENAME = "demo.txt"  # expected 286
FILENAME = "input.txt"

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def main() -> None:
    ship = 0, 0
    waypoint = -1, 10
    with open(FILENAME, "r") as file:
        for line in file:
            dist = int(line[1:])
            if line[0] == "F":
                ship = ship[0] + dist * waypoint[0], ship[1] + dist * waypoint[1]
            elif line[0] == "N":
                waypoint = waypoint[0] - dist, waypoint[1]
            elif line[0] == "S":
                waypoint = waypoint[0] + dist, waypoint[1]
            elif line[0] == "W":
                waypoint = waypoint[0], waypoint[1] - dist
            elif line[0] == "E":
                waypoint = waypoint[0], waypoint[1] + dist
            elif line[0] == "R":
                if dist == 90:
                    waypoint = waypoint[1], -waypoint[0]
                elif dist == 180:
                    waypoint = -waypoint[0], -waypoint[1]
                elif dist == 270:
                    waypoint = -waypoint[1], waypoint[0]
                else:
                    print(f"dist = {dist}")
                    raise NotImplementedError
            elif line[0] == "L":
                if dist == 90:
                    waypoint = -waypoint[1], waypoint[0]
                elif dist == 180:
                    waypoint = -waypoint[0], -waypoint[1]
                elif dist == 270:
                    waypoint = waypoint[1], -waypoint[0]
                else:
                    print(f"dist = {dist}")
                    raise NotImplementedError
            else:
                print(f"line[0] = {line[0]}")
                raise NotImplementedError
            print(line[:-1], f"ship = {ship}", f"waypoint = {waypoint}")
    print(abs(ship[0]) + abs(ship[1]))


if __name__ == "__main__":
    main()
