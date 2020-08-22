cars = ['audi', 'bmw', 'subaru', 'toyota']

# Print car names in title, except when it's BMW
for car in cars :
    if car == 'bmw' :
        print(car.upper())
    else:
        print(car.title())

# Python is case sensitive, none of the cars in the list are 'BMW', so all false
for car in cars :
    if car == 'BMW' :
        print("True\n")
    else:
        print("False\n")

# Now we convert the case to upper to get a true value for the 'bmw' in the list
for car in cars :
    if car.upper() == 'BMW' :
        print("True\n")
    else:
        print("False\n")
