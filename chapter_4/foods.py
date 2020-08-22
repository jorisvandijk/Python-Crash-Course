my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # copy the list

my_foods.append('canolli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

print("\nMy favorite foods are:")
for my_food in my_foods :
    print(my_food.title())

print("\nMy friends faavorite foods are:")
for friend_food in friend_foods :
    print(friend_food.title())
