FILENAME = "demo.txt"  # expected 514579
FILENAME = "input.txt"

TARGET = 2020


def main() -> None:
    expenses = []
    is_found = False
    with open(FILENAME, "r") as file:
        for line in file:
            expenses.append(int(line.strip()))
            for i in range(1, len(expenses) - 1):
                for j in range(i):
                    if expenses[i] + expenses[j] + expenses[-1] == TARGET:
                        print(expenses[i] * expenses[j] * expenses[-1])
                        is_found = True
                        break
                if is_found:
                    break
            if is_found:
                break


if __name__ == "__main__":
    main()
