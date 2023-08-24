number = int(input())

for n in range(number):
    asking_number = int(input())
    if asking_number == 88:
        print("Hello")
    elif asking_number == 86:
        print("How are you?")
    elif asking_number < 88 and asking_number != 86:
        print("GREAT!")
    elif asking_number > 88:
        print("Bye.")
