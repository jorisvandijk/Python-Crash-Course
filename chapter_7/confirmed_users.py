# Starts with users that need to be varifies
# and an empty list to hold users.
unconfirmed_users = ['alice', 'brian', 'lieke']
confirmed_users = []

# Verify each user until there are no more unconfirmed_users.
# Move each varified user to the confirmed_users list.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed:\n")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
