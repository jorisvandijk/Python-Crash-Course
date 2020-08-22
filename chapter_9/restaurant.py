class Restaurant:

    def __init__(self, name, type, open):
        """Define restaurant name and type."""
        self.name = name
        self.type = type
        self.open = open

    def describe_restaurant(self):
        """Print restaurant name and cuisine."""
        print(f"{self.name.title()} servers {self.type.title()} cuisine.")

    def opened_restaurant(self):
        """Check if the place is opened"""
        if self.open == True:
            print(f"{self.name.title()} is open!")

        else:
            print(f"Sorry, {self.name.title()} is closed today.")

chico = Restaurant('chicko', 'kebab', True)
carpaccio_bar = Restaurant('carpaccio bar', 'carpaccio', False)
mc_donalds = Restaurant('mc donalds', 'fast food', True)

chico.describe_restaurant()
chico.opened_restaurant()

carpaccio_bar.describe_restaurant()
carpaccio_bar.opened_restaurant()

mc_donalds.describe_restaurant()
mc_donalds.opened_restaurant()
