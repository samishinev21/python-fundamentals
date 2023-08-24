number_0 = int(input())
number_1 = int(input())
number_2 = int(input())

if number_0 > number_1 and number_0 > number_2:
    print(number_0)
elif number_1 > number_0 and number_1 > number_2:
    print(number_1)
else:
    print(number_2)