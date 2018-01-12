""" Examples on tuples"""

dimensions = (200, 50)
#print(dimensions[0])
#print(dimensions[1])

#looping through a tuple
print("Original dimensions")
for dimension in dimensions:
    print(dimension)

#writing over a tuple
dimensions = (300, 20)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)
