number = input("Tell me a number and I'll tell you if it is a multiple of 10\n:")
# Convert from a string to an intiger
number = int(number)

# when the number fits an x amount of times in ten and nothing is left over,
# the number has to be a multiple of 10.
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10!")

else:
    print(f"The number {number} is not a multiple of 10.")
