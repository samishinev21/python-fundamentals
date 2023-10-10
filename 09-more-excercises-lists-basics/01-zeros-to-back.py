list_str = input()
result = []
list = list_str.split(", ")
count_of_zeros = 0

for num in list:
    if num == "0":
        count_of_zeros += 1
    else:
        result.append(int(num))

result = result + [0] * count_of_zeros
print(result)