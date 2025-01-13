from __future__ import annotations

FILENAME = "demo.txt"
# FILENAME = "input.txt"


def main():
    result = 0
    with open(FILENAME, "r") as file:
        for line in file:
            print(line)
    print(result)


if __name__ == "__main__":
    main()
