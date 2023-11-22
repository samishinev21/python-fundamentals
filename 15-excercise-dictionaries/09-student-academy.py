n = int(input())
grades = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name in grades:
        grades[name].append(grade)
    else:
        grades[name] = [grade]

for (name, notes) in grades.items():
    avg = sum(notes) / len(notes)

    if avg >= 4.50:
        print(f"{name} -> {avg:.2f}")