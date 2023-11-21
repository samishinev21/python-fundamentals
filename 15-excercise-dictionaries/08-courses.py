registered = {}

while True:
    command = input()

    if command == "end":
       break

    tokens = command.split(" : ")
    course_name = tokens[0]
    student_name = tokens[1]

    if course_name in registered:
        registered[course_name].append(student_name)
    else:
        registered[course_name] = [student_name]

for (course_name, students) in registered.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")