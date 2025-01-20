FILENAME, LEN_PREAMBLE = "demo.txt", 5  # expected 62
FILENAME, LEN_PREAMBLE = "input.txt", 25


def main() -> None:
    preamble: list[int] = []
    with open(FILENAME, "r") as file:
        for line in file:
            if len(preamble) < LEN_PREAMBLE:
                preamble.append(int(line))
            else:
                current = int(line)
                found_flag = False
                for i in range(len(preamble) - LEN_PREAMBLE + 1, len(preamble)):
                    for j in range(len(preamble) - LEN_PREAMBLE, i):
                        if preamble[i] + preamble[j] == current:
                            found_flag = True
                            break
                    if found_flag:
                        break
                if not found_flag:
                    break
                preamble.append(current)
    print(current)
    for i in range(len(preamble)):
        current_sum = preamble[i]
        min_value = preamble[i]
        max_value = preamble[i]
        j = i + 1
        while j < len(preamble) and current_sum < current:
            current_sum += preamble[j]
            min_value = min(min_value, preamble[j])
            max_value = max(max_value, preamble[j])
            j += 1
        if current_sum == current:
            break
    print(min_value, max_value)
    print(min_value + max_value)


if __name__ == "__main__":
    main()
