locations = ['Fiji', 'Canada', 'USA', 'Amazon', 'Russia']
print(locations)

print("Sorted list: ")
print(sorted(locations))

print("\nOriginal list: ")
print(locations)

print("List in reverse alphabetical order: ")
print(sorted(locations, reverse=True))

locations.reverse()
print("\nList is reversed permanently: ")
print(locations)


locations.reverse()
print("\nList is back to the original state  ")
print(locations)

print("\n List is sorted permanently")
locations.sort()
print(locations)

print("\n List is sorted permanently in reverse alphabetical order")
locations.sort(reverse=True)
print(locations)
