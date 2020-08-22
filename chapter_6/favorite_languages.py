favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Let's list all items in the dictionary with their values
# Do not forget the .items() part to loop the items in the slist!
for k, v in favorite_languages.items():
    print(f"\n{k.title()}'s favorite language is {v.title()}.")

# You can also name the values 'k' and 'v' to anything, really...
for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

# Use the .keys() to list only the keys
for name in favorite_languages.keys():
    print(name.title())

# This command is the same as the above one as "key's" is the default behaviour.
for name in favorite_languages:
    print(name.title())

# Send a special message to our friends in the dictionary.
friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f"Hi, {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Check if Erin is in the dictionary and if not, ask her to take the poll
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our Poll!")

# Loop through the list in alphabetical order "sorted()"
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

print("The following languages have been mentioned:")

# Print all the mentioned languages
for language in favorite_languages.values():
    print(language.title())

print("\n")

# Print all the languages, but check for doubles with set()
for language in set(favorite_languages.values()):
    print(language.title())

print("\n")

# Print all the languages, but check for doubles with set() and sort the list
for language in sorted(set(favorite_languages.values())):
    print(language.title())
