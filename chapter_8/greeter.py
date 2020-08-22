def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}!")

def get_formatted_name(first, last):
    """Return full name neatly formatted"""
    name = f"{first} {last}"
    return name.title()


greet_user('jesse')
greet_user('sarah')

while True:
    print("Please tell me your name")
    print("Enter 'q' at any time to quit.")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name= input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello {formatted_name}!\n")
