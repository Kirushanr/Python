def get_sandwiches(*items):
    """ Prints summary of sandwiches that's being ordered"""
    print("\nSandwiches ordered: ")
    for value in items:
        print("-" + value)

get_sandwiches("egg", "fish")
get_sandwiches("egg", "bacon", "potatto")
