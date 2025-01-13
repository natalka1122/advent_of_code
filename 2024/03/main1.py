import re

def f(line):
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    result = 0
    for n1, n2 in regex.findall(line):
        print(n1, n2)
        result += int(n1)*int(n2)
        # print(regex.match(mul))
    return result

def main():
    result = 0
    with open('input.txt', 'r') as file:
    #with open('demo1.txt', 'r') as file:
        for line in file:
            result += f(line)
    print(result)

if __name__ == "__main__":
    main()