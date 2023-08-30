event = ""
coffees = 0

while event != "END":
    event = input()

    if (event.lower() == "coding" or event.lower() == "dog"
         or event.lower() == "cat" or event.lower() == "movie"):
        if event.isupper():
            coffees += 2
        else:
            coffees += 1
            
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)