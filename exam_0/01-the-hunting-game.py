days = int(input())
players = int(input())
groups_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())

total_water = water_per_day * players * days
total_food = food_per_day * players * days
 
for day in range(1, days + 1):
    enrgy_per_day = float(input())
    groups_energy -= enrgy_per_day

    if groups_energy <= 0:
        break

    if day % 2 == 0:
        total_water -= total_water * 30 / 100
        groups_energy += groups_energy * 5 / 100

    if day % 3 == 0:
        total_food -= total_food / players
        groups_energy += groups_energy * 10 / 100

if groups_energy > 0:
    print(f"You are ready for the quest. You will be left with - {groups_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")