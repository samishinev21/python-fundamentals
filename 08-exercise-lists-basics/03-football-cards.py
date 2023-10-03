Team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards_string = input()
cards = cards_string.split(" ")

for card in cards:
    team, player = card.split("-")
    if team == "A" and int(player) in Team_A:
        Team_A.remove(int(player))
    elif team == "B" and int(player) in Team_B:
        Team_B.remove(int(player))


print(f"Team A - {len(Team_A)}; Team B - {len(Team_B)}")
if len(Team_A) < 7 or len(Team_B) < 7:
    print("Game was terminated")