deck_str = input()
shuffles = int(input())

deck = deck_str.split(" ")

for _ in range(shuffles):
    mid = len(deck) // 2
    shuffled_deck = []

    for i in range(0, mid):
        shuffled_deck.append(deck[i])
        shuffled_deck.append(deck[mid])
        mid += 1

    deck = shuffled_deck
    

print(deck)