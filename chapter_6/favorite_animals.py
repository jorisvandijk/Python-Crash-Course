favorite_animal = {
    'jen': 'python',
    'sarah': 'mouse',
    'edward': 'horse',
    'phil': 'elephant'
    }

people_to_poll = ['jimmy', 'jen', 'sarah', 'tommy', 'edward', 'mike', 'phil']

if favorite_animal:
    for person in sorted(people_to_poll):
        if person in favorite_animal:
            print(f"Thanks {person.title()}. Your favorite animal is: {favorite_animal[person]}")

        else:
            print(f"{person.title()}, please take our poll!")
else:
    print("Nobody took the poll yet!")
