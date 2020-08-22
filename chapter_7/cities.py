prompt = "Enter a city you have visited.\n:"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    elif city == 'help':
        print("Typing 'quit' ends this program.")
    else:
        print(f"\nI'd love to visit {city.title()}!\n")
