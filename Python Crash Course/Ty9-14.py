from random import randint
""" Generates random integer number"""


class Die():
    def __init__(self, sides=6):
        """Initialize the die"""

        self.sides = sides

    def roll_die(self):
        """Roll the die and return the number on the face"""
        return randint(1, self.sides)

# six face die
results = []
six_side = Die(6)
print("6 side die \n")
for x in range(0, 6):
    results.append(six_side.roll_die())
print(results)

# 10 faces die
print("\n10 side die \n")
ten_side = Die(10)
results = []
for x in range(0, 10):
    results.append(ten_side.roll_die())
print(results)

# 20 faces die
print("\n20 side die")
twenty_side = Die(10)
results = []
for x in range(0, 20):
    results.append(twenty_side.roll_die())
print(results)
