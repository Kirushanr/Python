alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)


aliens = [] # an empty list

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)  # add new dictionary to end of the list

#print first five elements in the list
for alien in aliens[:5]:
    print(alien)

print("\nTotal number of aliens: " + str(len(aliens)))
