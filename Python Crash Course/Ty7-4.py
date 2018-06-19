prompt = "\nEnter your favorite pizza toppings"
prompt += "\nEnter 'quit to exit the program: "

flag = True

while flag:
    topping = input(prompt)  # Get the user's favorite topping
    #check the user has entered quit
    if topping.strip() == 'quit':
        flag = False
    else:
        #print the topping has been added
        print("We have added " + topping + "topping to your pizza")
