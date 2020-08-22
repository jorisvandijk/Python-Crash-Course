numbers = list(range(21))
print(numbers)

numbers = list(range(1000001))
print(max(numbers))
print(min(numbers))

print(sum(numbers))

numbers = list(range(1, 21, 2))
for number in numbers:
	print(number)

threes = list(range(0, 31, 3))
for three in threes:
	print(three)
print("cut here\n")

for cube in range(11):
	print(cube**3)


print("second cut here\n")
# Cubes equals [cube value]**3 (meaning value cubed) for [cube value] within the range 0 to 11

cubes = [cube**3 for cube in range(11)]
for cube in cubes:
	print(cube)

squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(f"squared in three lines of code: {squares}")

