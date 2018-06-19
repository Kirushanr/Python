number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is multiple of 10")
else:
    print("The number " + str(number) + " is not a multiple of 10")