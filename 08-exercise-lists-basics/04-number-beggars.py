money_str = input()
number_beggars = int(input())

beggars = [0] * number_beggars

money = money_str.split(", ")

while len(money) > 0:
    for i in range(number_beggars):
        if len(money) == 0:
            break
        beggars[i] += int(money.pop(0))
print(beggars)