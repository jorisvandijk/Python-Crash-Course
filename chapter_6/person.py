# Personal info
personal_information = {'first_name': 'jimmy', 'last_name': 'carr', 'occupation': 'comedian', 'age': '40'}

print(f"Hello, my name is {personal_information['first_name'].title()} {personal_information['last_name'].title()}. I am a {personal_information['occupation']} and I am {personal_information['age']} years old.")

# This could be cleaner...

name = f"{personal_information['first_name'].title()} {personal_information['last_name'].title()}"
job = personal_information['occupation']
age = personal_information['age']

print(f"Hello, my name is {name}. I am a {job} and I am {age} years old.")

# Fav numbers
favorite_numbers = {
    'jimmy': '14',
    'lenny': '21',
    'jeffrey': '10',
    'ellis': '3',
    'mark': '7'
}

print(f"Jimmy's favorite number is {favorite_numbers['jimmy']}.")
print(f"Lenny's favorite number is {favorite_numbers['lenny']}.")
print(f"Jeffrey's favorite number is {favorite_numbers['jeffrey']}.")
print(f"Ellis's favorite number is {favorite_numbers['ellis']}.")
print(f"Marks's favorite number is {favorite_numbers['mark']}.")

# Somehow that should be doable with one command wich also grabs the name...
# A little StackOverflow searching later:

print("\n This should be a simple command... \n")

# k stands for 'key', v for 'value'
for k, v in favorite_numbers.items():
    print(f"{k.title()}'s favorite number is {v}.")
