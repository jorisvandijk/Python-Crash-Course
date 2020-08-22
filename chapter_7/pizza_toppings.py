prompt = "Please add a topping for your pizza. When you're done, type 'quit'.\n:"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    else:
        print(f"\n{topping.title()} has been added to your pizza!\n")
