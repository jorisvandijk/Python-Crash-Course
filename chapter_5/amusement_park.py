age = 66

if age < 4:
    print("Admission is free for this child!")
elif age < 18 :
    print("Admission is $25 for this person.")
else:
    print("Admission is $40 for this person.")

# Or a little cleaner

if age < 4:
    admission = 0
elif age < 18:
    admission = 25
elif age < 65:
    admission = 40

# The following can be:
# else:
#     admission = 20
# or

elif age >= 65:
    admission = 20
print(f"Your admission is ${admission}.")
