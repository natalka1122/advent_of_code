from __future__ import annotations

FILENAME = "demo1.txt"  # expected 0
FILENAME = "input.txt"


def main():
    with open(FILENAME, "r") as file:
        for line in file:
            print(line.count("(") - line.count(")"))


if __name__ == "__main__":
    main()
