banned_users=['andrew','marie','david']
user = 'caroline'

if user not in banned_users:
    print(f"{user.title()}, you can comment if you like!")

# Booleans

if banned_users != 'andrew':
    print("Andrew is banned!\n")

print(user == 'marie')
print("The above should return a False")

print(user == 'caroline')
print("And this should be True")
