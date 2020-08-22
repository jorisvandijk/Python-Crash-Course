pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# Loop through the list to remove all instances of cats untill all are gone.
while 'cat' in pets:
    pets.remove('cat')

print(pets)
