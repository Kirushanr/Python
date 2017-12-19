
# Extra reading about time complexity of these operations 
# reference https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt

people = ['Albus', 'Fred', 'Lupin']

print("You're invited to Dinner " + people[0])
print("You're invited to Dinner " + people[1])
print("You're invited to Dinner " + people[2])


print(people[1]+" won't be able to attend the Ball \n")
people[1] = 'Tonks'

print("\nYou're invited to Dinner " + people[0])
print("\nYou're invited to Dinner " + people[1])
print("\nYou're invited to Dinner " + people[2])

print("\nWe have found large table for the dinner so we'll be having more guests tonight")

#insert requires two parameters, the index and the value that needs to be inserted into the list 

people.insert(0, 'Snape')
people.insert(2, 'James')
people.append('Lilly')

print("\nYou're invited to Dinner " + people[0])
print("\nYou're invited to Dinner " + people[1])
print("\nYou're invited to Dinner " + people[2])
print("\nYou're invited to Dinner " + people[3])
print("\nYou're invited to Dinner " + people[4])
print("\nYou're invited to Dinner " + people[5])


print("\nWe can only invite two people for dinner")
print(people)
#pop always removes the element from the end of the array according to LIFO principle

print("Sorry "+people.pop(4)+" we are unable to invite you to the dinner today")
print(people)
print("Sorry "+people.pop()+" we are unable to invite you to the dinner today")
print(people)
print("Sorry "+people.pop()+" we are unable to invite you to the dinner today")
print("Sorry "+people.pop()+" we are unable to invite you to the dinner today\n\n")

print("\nYou're still invited to Dinner " + people[0])
print("\nYou're still invited to Dinner " + people[1])

del people[0]
del people[0]

print(people)
