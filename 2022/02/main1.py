FILENAME = "demo.txt"  # expected 15
FILENAME = "input.txt"

R, P, S = "R", "P", "S"
WIN = "SRPS"
OPP = {"A": R, "B": P, "C": S}
ME = {"X": R, "Y": P, "Z": S}
SCORE = {R: 1, P: 2, S: 3}


def f(line: list[str]) -> int:
    if len(line) != 2:
        raise NotImplementedError
    opp_move = OPP[line[0]]
    me_move = ME[line[1]]
    if opp_move == me_move:
        return SCORE[me_move] + 3
    if opp_move + me_move in WIN:
        return SCORE[me_move] + 6
    return SCORE[me_move]


def main() -> None:
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            result += f(list(line.strip().split(" ")))
    print(result)


if __name__ == "__main__":
    main()
