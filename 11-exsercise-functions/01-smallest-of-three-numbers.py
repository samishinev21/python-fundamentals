num_0 = int(input())
num_1 = int(input())
num_2 = int(input())

def smallest(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
    
print(smallest(num_0, num_1, num_2))