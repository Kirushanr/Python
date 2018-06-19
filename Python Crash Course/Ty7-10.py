dream_vacation = {}

flag = True

while flag:
    name = input("Enter your name : ")
    vacation = input("If you could visit one place in the world, where would you go: ")
    dream_vacation[name] = vacation

    response = input("Would you like to let another person respond (yes/no): ")
    if response == 'yes':
        flag = False


for name, response in dream_vacation.items():
    print("\n" + name + " wants to visit " + response)
