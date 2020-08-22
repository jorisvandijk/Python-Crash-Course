jimmy = {'first_name': 'jimmy', 'last_name': 'carr', 'occupation': 'panel show host', 'age': '40'}
dara = {'first_name': 'dara', 'last_name': 'o briain', 'occupation': 'comedian', 'age': '35'}
jon = {'first_name': 'jon', 'last_name': 'richardson', 'occupation': 'panel show team leader', 'age': '30'}

people = [jimmy, dara, jon]

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    occupation = person['occupation']
    age = person['age']

    print(f"This is {name}, {age} years old and he's a {occupation}.")
