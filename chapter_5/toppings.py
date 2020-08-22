# "Is not equal to" test !=
first_requested_topping = 'mushrooms'

if first_requested_topping != 'anchovies' :
    print("Hold the anchovies!\n")

# Continuation

#requested_toppings = ['mushroom', 'green peppers', 'extra cheese']
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we're out of green peppers!")
        else:
            print(f"Adding {requested_topping}")
else:
    print("Are you sure you want a plain pizza?")

print("\nYour pizza is finished!\n")
