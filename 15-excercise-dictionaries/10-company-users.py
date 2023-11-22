companies = {}

while True:
    command = input()

    if command == "End":
        break

    tokens = command.split(" -> ")
    company_name = tokens[0]
    employee_id = tokens[1]

    if company_name in companies:
        companies[company_name].append(employee_id)
    else:
        companies[company_name] = [employee_id]

for (name, identifications) in companies.items():
     print(name)
     for identification in set(identifications):
         print(f"--{identification}")