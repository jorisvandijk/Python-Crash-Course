"""list
display one item
witch caps without title
add to the list in specific place
append to list
insert into list
del item
pop item
show popped item
remove by value

sorted temp sort
sort list
reverse sort
reverse
show length
"""

candy = ['spekje', 'drop', 'chocolade', 'lolly', 'gummybeer']

print(candy)
print(candy[1])
print(candy[0].title())
print(candy[0].upper())
print(candy[0].lower())

candy.append('salmiak')
print(candy)

candy.insert(0, 'wiebertjes')
print(candy)

del candy[2]
print(candy)

popped_candy = candy.pop(2)
print(popped_candy)

candy.remove('gummybeer')
print(candy)

print(sorted(candy))
print(candy)


