# Lists inside dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

# Get names and languages
for name, languages in favorite_languages.items():

    # Check if a list only holds one item
    if len(languages) == 1:

        # Print name
        print(f"\n{name.title()}'s favorite languages is:")

            # Print the one listed language per name
        for language in languages:
            print(language.title())
    else:
        # Print name
        print(f"\n{name.title()}'s favorite languages are:")

        # Print all listed languages per name
        for language in languages:
            print(language.title())
