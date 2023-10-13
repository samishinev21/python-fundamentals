oparation = input()
num_0 = int(input())
num_1 = int(input())

def calculate(a, oparation, b):
     
    if oparation == "multiply":
        return a * b
    elif oparation == "divide":
        return a / b
    elif oparation == "add":
        return a + b
    elif oparation == "subtract":
        return a - b

print(int(calculate(num_0, oparation, num_1)))
