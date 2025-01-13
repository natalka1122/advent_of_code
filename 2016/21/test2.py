result = "bcdeax"
print(result)
v1 = 1
v2 = 4
result = result[:v1] + result[v1 + 1 : v2 + 1] + result[v1] + result[v2 + 1 :]
print(result)
result = result[:v1] + result[v2] + result[v1:v2] + result[v2 + 1 :]
print(result)


result = "bcdeax"
print(result)
v1 = 4
v2 = 1
result = result[:v2] + result[v1] + result[v2:v1] + result[v1 + 1 :]
print(result)
result = result[:v2] + result[v2 + 1 : v1 + 1] + result[v2] + result[v1 + 1 :]
print(result)
