magicians = ['allice', 'david', 'carolina']
for magician in magicians:
	print(magician)

people = ['joris', 'lieke', 'andrea']
for person in people:
	print(person)

print('\n')

for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}!\n")

print("Thank you everyone, that was a great magic show!")

magicians = ['allice', 'david', 'carolina']
for magician in magicians:
	print(magician)

print("\n - break -\n")

for magician in magicians[:2] :
	print(magician.title())

for magician in magicians[1:2] :
	print(magician.title())

for magician in magicians[-1:] :
	print(f"The last magician is {magician.title()}")
