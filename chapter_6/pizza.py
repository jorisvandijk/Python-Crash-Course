# Store information bout a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# Summerize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
    
for topping in pizza['toppings']:
    print(f"\t{topping}")
