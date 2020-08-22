responses = {}

# Set flag to indicate polling is active.
polling_active = True

while polling_active:
    # Prompt user for name and response.
    name = input("What is your name?\n:")
    response = input("\nWhat mountain would you like to climb?\n:")

    # Store response in dictionary.
    responses[name] = response

    # Find out if anyone else is taking the poll.
    repeat = input("\nWould anyone else like to take the poll? (yes/no)\n:")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results --- \n")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")
