def check_for_safety(report):
    print(f"== {report}")
    if len(report) < 2:
        return True
    if report[0]==report[1] or abs(report[0]-report[1]) > 3:
        print("unsafe 0")
        return False
    multiplier = int(abs(report[0]-report[1])/(report[0]-report[1]))
    for i in range(1, len(report)-1):
        if multiplier*(report[i]-report[i+1])<1 or multiplier*(report[i]-report[i+1])>3:
            print(f"unsafe {i}")
            return False
    return True


def main():
    safe_count = 0
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            report = list(map(int, line.split(" ")))
            print(report, end=" ")
            if check_for_safety(report):
                safe_count += 1
                continue
            is_safe = False
            for i in range(len(report)):
                if check_for_safety(report[:i]+report[i+1:]):
                    is_safe = True
                    break
            if is_safe:
                print("safe")
                safe_count += 1


    
    print(safe_count)


if __name__ == "__main__":
    main()
