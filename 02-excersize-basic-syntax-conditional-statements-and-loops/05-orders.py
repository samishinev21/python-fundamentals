number_of_orders = int(input())
total_price = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    order_price = price_per_capsule * days * capsules_needed_per_day
    total_price += order_price
    print("The price for the coffee is: $%.2f" % order_price)
print("Total: $%.2f" % total_price)   
