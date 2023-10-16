def sum_numbers(a, b):
    return a + b

def subtract(a, b):
    return a - b

def add_and_subtract(a, b, c):
    x = sum_numbers(a, b)
    return subtract(x, c)

initial_num = int(input())
add_num = int(input())
subtract_num = int(input())

print(add_and_subtract(initial_num, add_num, subtract_num))