str = input()

list_of_numbers_str = str.split(" ")
list_of_float = []
list_of_abs = []

for float_num_str in list_of_numbers_str:
    list_of_float.append(float(float_num_str))

for n in list_of_float:
    list_of_abs.append(abs(n))

print(list_of_abs)