def main():
    result = 0
    array1 = []
    array2 = []
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            n1,n2 = line.split("   ")
            array1.append(int(n1))
            array2.append(int(n2))
    
    array1 = sorted(array1)
    array2 = sorted(array2)
    print(array1,array2)
    result = 0
    for i in range(len(array1)):
        result += abs(array1[i]-array2[i])
    print(result)


if __name__ == "__main__":
    main()
