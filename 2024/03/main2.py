import re

def f(line):
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")
    result = 0
    to_do = True
    for n1, n2, do, dont in regex.findall(line):
        if do:
            to_do = True
        elif dont:
            to_do = False
        elif to_do:
            result += int(n1)*int(n2)
    return result

def main():
    with open('input.txt', 'r') as file:
    #with open('demo2.txt', 'r') as file:
        print(f(" ".join(file.readlines())))

if __name__ == "__main__":
    main()