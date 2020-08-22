motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('bmw')
print(motorcycles)

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0, 'ducati')

print(motorcycles)

del motorcycles[2]

print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = popped_motorcycle

print(f"The last motorcycle I've owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I've owned was a {first_owned.title()}.")

print(motorcycles)

motorcycles = ['bmw', 'honda', 'kawasaki']
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['bmw', 'honda', 'kawasaki', 'ducati']
too_expensive = 'ducati'
print(motorcycles)
motorcycles.remove(too_expensive)

print(f"\nA {too_expensive.title()} was too expensive for me.")
print(motorcycles)