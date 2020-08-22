availible_toppings = ['mushrooms', 'salami', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availible_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we do not have {requested_topping}!")

print("\nYour pizza is ready!")
