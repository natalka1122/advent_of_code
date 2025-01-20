FILENAME = "demo1.txt"  # expected 2
FILENAME = "input.txt"
FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def f(passport: set[str]) -> bool:
    for field in FIELDS:
        if field not in passport:
            return False
    return True


def main() -> None:
    result = 0
    current_passport: set[str] = set()
    with open(FILENAME, "r") as file:
        for line in file:
            if len(line) == 1:
                if f(current_passport):
                    result += 1
                current_passport = set()
            else:
                for field in FIELDS:
                    if f"{field}:" in line:
                        current_passport.add(field)
    if f(current_passport):
        result += 1
    print(result)


if __name__ == "__main__":
    main()
