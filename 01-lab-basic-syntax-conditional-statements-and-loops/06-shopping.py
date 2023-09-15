budget = int(input())
command = input()

while command != "End":
    price_products = int(command)
    budget -= price_products
    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought evrything you need.")