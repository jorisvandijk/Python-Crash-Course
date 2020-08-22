fruits = ['apple','pear','kiwi']

if 'apple' in fruits:
    print("An apple is a fruit.")

my_favorite_fruit = "orange"

if my_favorite_fruit not in fruits:
    print("Your favorite fruit is not in the fruitbowl today!")

my_favorite_fruit = "kiwi"
if my_favorite_fruit in fruits:
    print(f"You're in luck, {my_favorite_fruit.title()} is in the fruitbowl!")

legal_age_alcohol = 18
my_age = 16

if my_age <= legal_age_alcohol:
    print("You're too young to drink, sorry!")

my_age = 23

if my_age >= legal_age_alcohol:
    print("Have a beer!")

kat = "siamees"
klap = "mep"

if kat == 'siamees':
    print("Miaauw")

if kat != 'mus' and klap != 'kus':
    print("Een kat is geen mus, een klap is geen kus.")


if kat == 'siamees' or klap == 'handdoek':
    print("This makes no sense, but it's an or-check.")


written_silly = "ELepHanT"

if written_silly.lower() == 'elephant':
    print("Don't let it loose in a China shop!")
