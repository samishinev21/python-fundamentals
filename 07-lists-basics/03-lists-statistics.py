count = int(input())
positives = []
negatives = []
sum_negatives = 0

for _ in range(count):
    number = int(input())
    if number < 0:
        negatives.append(number)
        sum_negatives += number
    else:
        positives.append(number)

count_positives = len(positives)

print(positives)
print(negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_negatives}")