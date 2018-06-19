prompt = "\nPlease enter your age, we will let you know the ticket price: "

active = 0

while active < 10:
    age = input(prompt)
    active += 1
    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif age >= 3 and age < 12:
        print("Your ticket is 10$")
    else:
        print("Your ticket price is 15$")

print("It's House Full")
