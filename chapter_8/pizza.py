def make_pizza(size, *toppings):
    """Summerize the pizza we're going to make."""
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Commented out in order to use this file as module.
#make_pizza('large', 'pepperoni')
#make_pizza('medium', 'mushrooms', 'green peppers', 'extra cheese')
