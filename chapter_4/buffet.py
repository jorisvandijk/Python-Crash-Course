foods = ('lasagne', 'pizza', 'pasta', 'meatloaf', 'steak')

print("This buffet includes:")
for food in foods :
    print(food.title())

# The following should create a not supported error
# foods[2] = 'sausage'

# Menu revisions!
foods = ('lasagne', 'sausage', 'pizza', 'steak', 'hamburgers')

print("\nOur menu has changed! We now offer:")
for food in foods :
    print(food.title())
