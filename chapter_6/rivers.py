rivers = {
    'nile': 'egypt',
    'amazon': 'brasil',
    'colorado river': 'usa'
}

if rivers:
    for river, country in sorted(rivers.items()):
        if country == 'usa':
            print(f"The {river.title()} runs through the {country.upper()}.")
        else:
            print(f"The {river.title()} runs through {country.title()}.")

    print("\nThe following rivers where mentioned:")
    for river in sorted(rivers):
        print(river.title())

    print("\nThe following countries where mentioned:")
    for country in sorted(rivers.values()):
        if country == "usa":
            print(f"The {country.upper()}")
        else:
            print(country.title())
else:
    print("No rivers listed!")
