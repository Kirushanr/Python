def make_pizza(*toppings):
    """ Print the list of toppings that have been requested. """
    print("\nMaking a pizza with the following topping")
    for topping in toppings:
        print("- " + topping)
