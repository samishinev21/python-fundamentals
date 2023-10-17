def is_even(num):
    if int(num) % 2 == 0:
        return True
    else:
        return False
    
nums = input()
digits = nums.split(" ")
result = list(filter(is_even, digits))

print(result)
