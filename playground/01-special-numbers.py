n = int(input())

for num in range(1, n + 1):
    sum_of_digits = 0
    digits = num

    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)

    is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11

    print(f"{num} -> {is_special}")
        
