order = input()
quantity = int(input())

def calculate(order, quantity):
    item_price = 0
    if order == "coffee":
        item_price = 1.50
    elif order == "water":
        item_price = 1.00
    elif order == "coke":
        item_price = 1.40
    elif order == "snacks":
        item_price = 2.00
    
    return item_price * quantity

print(calculate(order, quantity))