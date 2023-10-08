list_str = input()
remove_count = int(input())

list = list_str.split(" ")

sorted_list = []

for num in list:
    sorted_list.append(int(num))

sorted_list.sort()

to_remove = sorted_list[:remove_count]

for num in to_remove:
    list.remove(str(num))

result = ", ".join(list)

print(result)