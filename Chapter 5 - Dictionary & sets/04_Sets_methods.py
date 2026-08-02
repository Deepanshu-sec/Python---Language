s = {1,2,3,4,5,6}

# len() --> Show the number of items.
print(len(s))

# add() --> Add an element in set.
s.add(7)
print(s)

# remove() --> Remove the element.
s.remove(7)
print(s)

# discard() --> also remove he element but if element does't exist then no error.
s.discard(11)
print(s)

# pop() --> Delete the random element.
s.pop()
print(s)

# update() --> Add multiple element.
s.update([7,8,9,10])
print(s)