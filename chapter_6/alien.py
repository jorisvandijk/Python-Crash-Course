alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x-position'] = 0
alien_0['y-position'] = 25

print(alien_0)

alien_0 = {}

print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print(f"The color of the alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'

print(f"The color of the alien is altered to {alien_0['color']}.")

# Reset alien and play on
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position of the alien is {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on it's specified
if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the x_increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position is {alien_0['x_position']}")

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Delete the points
del alien_0['points']

print(alien_0)
