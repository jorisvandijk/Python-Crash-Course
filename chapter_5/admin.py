#users = ['admin', 'lieke', 'marlies', 'justin', 'andrea']
users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello Admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}")
else:
    print(f"We need more users!")

print("\nUsername checking:\n")

# List of current users in all sorts of cases
current_users = ['ADMIN', 'lieke', 'MARlies', 'JUSTIN', 'andrea']

# Newly registering users, not case sensitive
new_users = ['JOOP', 'lia', 'marLIES', 'ronnie', 'justin']

if current_users:

    # Convert list to lowercase version to use in check
    for current_user in current_users:
        current_users_lower = [current_user.lower() for current_user in current_users]

    # Check if new user name converted in lowercase is already in the lowercase username list
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f"{new_user} is already registered!")
        else:
            print(f"Welcome {new_user}!")

else:
    print("No users registered.")
