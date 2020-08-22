# This is not functional at the moment. It should ask a few questions,
# add them to the dictionary and eventually print all of them.

class Users:
    def __init__(self, username, name, url, shown):
        """Collect data for a list of websites"""
        self.name = name
        self.url = url
        self.username = username
        self.shown = shown

    def show_listing(self):
        """Show the website listing fully or not"""
        if self.shown == 'yes':
            print(f"{self.username} added {self.name}, which is found here: "
                f"{self.url}.")
        else:
            print(f"An anonymous user added {self.name}, which can be found"
                    f"here: {self.url}.")
responses = {}

while True:
        print("\nWe're gathering responses. Any user may add one.")
        username = input("Please enter your username.\n:")
        name = input("Please enter your website name.\n:")
        url = input("Please enter your website url.\n:")
        shown = input("Do you want this to be posted with your name? (yes/no)\n:")

        cont = input("Will another user add a site? (yes/no)")
        if cont == 'no':
            break

for response in responses:
    reply = Users(username, name, url, shown)
    reply.show_listing()
