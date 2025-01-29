my_ans = "a2582a3ae66e6e86e3812dcb672a272"
correct = "a2582a3a0e66e6e86e3812dcb672a272"

print(len(my_ans))
print(len(correct))
# result = []
# for i in range(len(a)//2):
#     result.append(int(a[i*2:i*2+2],16))
# print(result)
print(hex(0).split("x")[1])
print(hex(2).split("x")[1])

dense_hash = [162, 88, 42, 58, 14, 102, 230, 232, 110, 56, 18, 220, 182, 114, 162, 114]
for i in range(len(dense_hash)):
        print(hex(dense_hash[i]).split("x")[1], end="")
print()