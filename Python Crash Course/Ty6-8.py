cat = {'type': 'mammal', 'owner':'Flitch', 'animal': 'cat'}
dog = {'type': 'mammal', 'owner':'Hagrid', 'animal': 'dog'}

pets = [cat, dog]

for pet in pets:
    print(pet['animal'].title() + " owned by " + pet['owner'])
 