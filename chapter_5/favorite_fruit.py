my_favorite_fruit = ['apple', 'pear', 'banana']

if 'apple' in my_favorite_fruit:
    print("You really love apple!")

if 'kiwi' in my_favorite_fruit:
    print("You really love kiw!")

if 'banana' in my_favorite_fruit:
    print("You really love banana!")

if 'orange' in my_favorite_fruit:
    print("You really love orange!")

if 'pear' in my_favorite_fruit:
    print("You really love pear!\n")

# Or with a loop for more efficiency

for fruit in my_favorite_fruit:
    print(f"You really love {fruit}!")
