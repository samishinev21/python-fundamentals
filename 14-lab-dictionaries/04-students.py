command = input()
courses = {}

while command != "programming_basics" and command != "fundamentals" and command != "advanced":
    tokens = command.split(":")
    name = tokens[0]
    id = tokens[1]
    course = tokens[2]
    course = course.replace(" ", "_")

    if course in courses:
        courses[course].append(f"{name} - {id}")
    else:
        courses[course] = [f"{name} - {id}"]
    
    command = input()

students_in_course = courses[command]

for student in students_in_course:
    print(student)