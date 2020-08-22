def describe_city(name, country='the netherlands'):
    """Describe a city."""
    print(f"{name.title()} is in {country.title()}")

describe_city('oss')
describe_city('new york', 'the united states of america')
describe_city(name='dublin', country='ireland')
