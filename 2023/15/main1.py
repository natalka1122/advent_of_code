from __future__ import annotations

# FILENAME = "demo.txt"
FILENAME = "input.txt"

def the_hash(line):
    result = 0
    for symbol in line:
        result += ord(symbol)
        result*= 17
        result = result%256
    return result

def main():
    result = 0
    with open(FILENAME, "r") as file:
        for line in file.readline().split(","):
            result += the_hash(line)
    print(result)


if __name__ == "__main__":
    main()
