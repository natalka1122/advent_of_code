def main():
    result = 0
    array1 = []
    the_dict = dict()
    with open('input.txt', 'r') as file:
    #with open('demo.txt', 'r') as file:
        for line in file:
            n1,n2 = line.split("   ")
            n1,n2 = int(n1), int(n2)
            array1.append(n1)
            if n2 in the_dict:
                the_dict[n2] += 1
            else:
                the_dict[n2] = 1
    
    print(array1,the_dict)
    result = 0
    for n in array1:
        if n in the_dict:
            result += n * the_dict[n]
    print(result)


if __name__ == "__main__":
    main()
