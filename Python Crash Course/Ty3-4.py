#This program has the Excersises from 3.4-3.6 

people = ['Albus','Fred','Lupin']

print("You're invited to Dinner " + people[0])
print("You're invited to Dinner " + people[1])
print("You're invited to Dinner " + people[2])



print (people[1]+" won't be able to attend the Ball \n")
people[1]='Tonks'

print("\nYou're invited to Dinner " + people[0])
print("\nYou're invited to Dinner " + people[1])
print("\nYou're invited to Dinner " + people[2])

print("\nWe have found large table for the dinner so we'll be having more guests tonight")

#insert requires two parameters, the index and the value that needs to be inserted into the list 

people.insert(0,'Snape'); #insert the guest to the top of the list
people.insert(2,'James'); #insert the guest to the middle of the list 
people.append('Lilly')

print("\nYou're invited to Dinner " + people[0])
print("\nYou're invited to Dinner " + people[1])
print("\nYou're invited to Dinner " + people[2])
print("\nYou're invited to Dinner " + people[3])
print("\nYou're invited to Dinner " + people[4])