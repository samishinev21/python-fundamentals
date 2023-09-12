list = input()

queue = list.split(", ")
queue_size = len(queue)

for i, animal in enumerate(queue):
    if animal == "wolf":
        if i == queue_size - 1:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {queue_size - (i + 1)}! You are about to be eaten by a wolf!")