motorcycles =[] #empty list
motorcycles.append('honda') # add an element to the end of the list 
motorcycles.insert(0,'yamaha')	#insert an element in the specified position
motorcycles.append('suzuki')


del motorcycles[0] #delete the element in position 
print(motorcycles)

print(motorcycles.pop()) #remove the last element from the list

print(motorcycles)
motorcycles.append('ducati')

print(motorcycles)
expensive_vehicle=motorcycles.pop(0);
print('Too expensive motorcycle '+ expensive_vehicle)