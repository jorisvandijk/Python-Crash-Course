users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    }, # Note the comma for seperating the two dictionaries in user dictionary
    'mcurrie': {
        'first': 'marie',
        'last': 'currie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")

    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
