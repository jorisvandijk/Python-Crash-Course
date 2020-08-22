sandwich_orders = ['pastrami', 'blt', 'cheese', 'pastrami', 'ham', 'pastrami',
    'filet americain', 'bacon and egg']
finished_sandwiches = []

print("Sorry, we're out of Pastrami sandwiches!\n")

# As long as there are sandwiches in sandwich_orders, loop.
while sandwich_orders:

    # Name items in sandwich_orders as sandwich.
    sandwich = sandwich_orders.pop()

    # Check for Pastrami in orders.
    if sandwich == 'pastrami':

        # Loop through sandwich_orders and remove all Pastrami orders.
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')

    # If the sandwich is a BLT, print in uppercase.
    elif sandwich == 'blt':
        print(f"I made a {sandwich.upper()} sandwich for you.")

        # Move this sandwich to the finished_sandwiches dictionary.
        finished_sandwiches.append(sandwich)

        # For all other sandwiches, write in title and move like above.
    else:
        print(f"I made a {sandwich.title()} sandwich for you.")
        finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")

# Name items in finished_sandwiches as sandwich.
for sandwich in finished_sandwiches:

    # If it isn't a BLT, print in title.
    if sandwich != 'blt':
        print(f"\t{sandwich.title()}")

    # If it is a BLT, write in upper.
    else:
        print(f"\t{sandwich.upper()}")
