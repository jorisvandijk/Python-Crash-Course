pizzas = ['pepperoni','hawaii', 'quattro stagoni']
for pizza in pizzas:
	print(f"I like {pizza.title()} pizza!")

print("I really love pizza!\n")

friend_pizzas = pizzas[:] #copy the full list to a new list

pizzas.append("diavola")
print(f"My favorite pizzas are:")
for pizza in pizzas :
	print(pizza.title())

print("\n")

friend_pizzas.append("magarita")
print(f"My friends favorite pizzas are:")
for friend_pizza in friend_pizzas :
	print(friend_pizza.title())
