prompt = "Please enter your age to get a ticket price.\n:"

age = input(prompt)
age = int(age)

if age < 3:
    price = 0

elif age < 12:
    price = 10

else:
    price = 15

print(f"The price of your ticket is ${price}.")
