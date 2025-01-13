def main():
    safe_count = 0
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            report = list(map(int, line.split(" ")))
            print(report, end=" ")
            if report[0]==report[1] or abs(report[0]-report[1]) > 3:
                print("unsafe 0")
                continue
            multiplier = int(abs(report[0]-report[1])/(report[0]-report[1]))
            is_safe = True
            for i in range(1, len(report)-1):
                if multiplier*(report[i]-report[i+1])<1 or multiplier*(report[i]-report[i+1])>3:
                    print(f"unsafe {i}, {multiplier} {multiplier*(report[i]-report[i+1])}")
                    is_safe = False
                    break
            if is_safe:
                print("safe")
                safe_count += 1


    
    print(safe_count)


if __name__ == "__main__":
    main()
