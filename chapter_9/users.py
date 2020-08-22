class User:
    # Get values
    def __init__(self, first_name, last_name, user_name, user_location, user_sex):
        """Define user information."""

        # Set easy to use values for use below
        self.first = first_name
        self.last = last_name
        self.username = user_name
        self.location = user_location
        self.sex = user_sex

    def describe_user(self):
        """Summarize user"""
        print(f"{self.username} is from {self.location.title()}.")

        # Check sex for his/her greeting
        if self.sex == 'male':
            print(f"{self.first.title()} {self.last.title()} is his full name.\n")
        else:
            print(f"{self.first.title()} {self.last.title()} is her full name.\n")

    def greet_user(self):
        """Personal greeting for user."""
        print(f"Hiya {self.username}!")

lieke = User('lieke', 'paijmans', 'lpaij', 'hollywood', 'female')
andrea = User('andrea', 'van dijk', 'adij', 'pisa', 'female')
justin = User('justin', 'van Orsouw', 'jors', 'berlin', 'male')

lieke.greet_user()
lieke.describe_user()

andrea.greet_user()
andrea.describe_user()

justin.greet_user()
justin.describe_user()
