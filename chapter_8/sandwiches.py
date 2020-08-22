def toppings(*toppings):
    """Storing and displaying what kind of toppings people want"""
    print("\nYour sandwich contains the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

toppings('onion', 'tomato', 'ham', 'bacon')
toppings('cheese', 'egg')
toppings('chicken', 'pineapple', 'lettuce')
