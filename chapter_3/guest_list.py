guests = ['julius ceasar', 'adolf hitler', 'alexander the great', 'ghengis kahn']

name = guests[0].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

name = guests[1].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

name = guests[2].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

name = guests[3].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.\n")

number = len(guests)
print(f"The number of guests is {number} currently.")


cannot_attend = guests.pop(1)
print(f"\n{cannot_attend.title()} cannot attend.\n")

guests.insert(1, 'montezuma II')

name = guests[1].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

print("\nI have found a bigger dinner table, so more people can attend!\n")

guests.insert(0, 'atilla the hun')
guests.insert(2, 'saladin')
guests.insert(-1, 'napoleon bonaparte')

name = guests[0].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

name = guests[1].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

name = guests[2].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

name = guests[3].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

name = guests[4].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

name = guests[5].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.")

name = guests[6].title()
print(f"Dear {name}, you are hereby cordially invited to my dinner party.\n")

number = len(guests)
print(f"The number of guests is {number} currently.")

print("\nUnfortunately the table will arrive too late, so I can only invite two people.\n")

guest = guests.pop(0).title()
print(f"Sorry {guest}, you cannot come.")

guest = guests.pop(1).title()
print(f"Sorry {guest}, you cannot come.")

guest = guests.pop(1).title()
print(f"Sorry {guest}, you cannot come.")

guest = guests.pop(1).title()
print(f"Sorry {guest}, you cannot come.")

guest = guests.pop(1).title()
print(f"Sorry {guest}, you cannot come.\n")

name = guests[0].title()
print(f"Dear {name}, you are still invited to my dinner party.")

name = guests[1].title()
print(f"Dear {name}, you are still invited to my dinner party.\n")

number = len(guests)
print(f"The number of guests is {number} currently.")

del guests[0]

print(guests)

del guests[0]

print(guests)

number = len(guests)
print(f"The number of guests is {number} currently.")

