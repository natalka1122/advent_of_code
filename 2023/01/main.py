import re

NUMBERS = ["one","two","three","four","five","six","seven","eight","nine"]
NUMBERS_DICT = dict()
for i in range(len(NUMBERS)):
    NUMBERS_DICT[NUMBERS[i]] = i+1
    NUMBERS_DICT[str(i+1)] = i+1
print(NUMBERS_DICT)

def f(line):
    print(line)
    digits = []
    for i in range(len(line)):
        for key in NUMBERS_DICT:
            #print(line[i:i+len(num)], num)
            if line[i:i+len(key)] == key:
                digits.append(NUMBERS_DICT[key])
                break
    print(digits)
    # result = re.findall(regex,line)
    # if result:
    #     print(result, result[0]+result[-1])
    #     return int(result[0]+result[-1])
    return 10*digits[0]+digits[-1] 

def main():
    result = 0
    with open('input.txt', 'r') as file:
    #with open('demo2.txt', 'r') as file:
        for line in file:
            result += f(line)
    print(result)

if __name__ == "__main__":
    main()