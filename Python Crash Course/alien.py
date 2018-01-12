alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 0

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

alien_0['color'] = 'yellow'
alien_0['speed'] = 'medium'

print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien basedon its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

del alien_0['points']

print(alien_0)
