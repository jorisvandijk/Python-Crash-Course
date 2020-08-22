# Function.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} is named {pet_name.title()}.")

# Function with default values.
def describe_pet_size(animal_height='20', animal_weight='10'):
    """Display information about a pet's size."""
    print(f"\nMy pet is {animal_height} centimeters tall.")
    print(f"My pet weighs {animal_weight} kilograms.")

# Positional aruments, order of the arguments matters.
describe_pet('hamster', 'harry')
describe_pet('dog', 'max')

# Keyword arguments, order doesn't matter.
describe_pet(animal_type='cat', pet_name='sally')
describe_pet(pet_name='lucy', animal_type='goldfish')

# Show the default values.
describe_pet_size()

# Overwrite default values.
describe_pet_size(animal_height='50', animal_weight='16')
