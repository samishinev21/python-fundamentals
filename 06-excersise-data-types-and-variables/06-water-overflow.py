num = int(input())
MAX_CAPACITY = 255
current_level = 0

for n in range(num):
    current_litters = int(input())
    if current_level + current_litters > MAX_CAPACITY:
        print("Insufficient capacity!")
    else:
        current_level += current_litters
print(current_level)