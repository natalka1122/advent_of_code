from __future__ import annotations

FILENAME = "input.txt"

MULTIPLIER = 100
SEVEN = 7


class Marble:
    def __init__(self, number: int, left: Marble | None = None, right: Marble | None = None):
        self.num = number
        self.left = self if left is None else left
        self.right = self if right is None else right

    def __repr__(self) -> str:
        return f"({self.left.num})->Marble({self.num})->({self.right.num})"


def f(players_count: int, last_marble_points: int) -> int:
    players_score = [0 for _ in range(players_count)]
    current = Marble(0)
    for step in range(1, last_marble_points * MULTIPLIER + 1):
        if step % 23 == 0:
            players_score[step % players_count] += step
            for _ in range(SEVEN - 1):
                current = current.left
            players_score[step % players_count] += current.left.num
            current.left = current.left.left
            current.left.right = current
        else:
            right1 = current.right
            right2 = right1.right
            current = Marble(step, left=right1, right=right2)
            right1.right = current
            right2.left = current

    return max(players_score)


def main() -> None:
    with open(FILENAME, "r") as file:
        for line in file:
            line_split = line.split(" ")
            print(f(int(line_split[0]), int(line_split[6])))
            # return


if __name__ == "__main__":
    main()
