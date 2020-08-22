current_number = 0

# Keep running the program as long as the current_number is less than 10.
while current_number < 10:

    # Add 1
    current_number += 1

    # If number is devidable by 2, 'continue to the beginning' and skip the
    # rest of the code below.
    if current_number % 2 == 0:
        continue

    # This is only executed if the current_number is not devidable by 2.
    print(current_number)

# In essance, this program prints only odd numbers under 10 and then quits.
