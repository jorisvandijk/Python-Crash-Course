for value in range(1, 6):
	print(value)

numbers = list(range(6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(f"squared in four lines of code: {squares}")

squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(f"squared in three lines of code: {squares}")

test = [number**2 for number in range(1, 11)]
print(f"squared in one line of code: {test}")