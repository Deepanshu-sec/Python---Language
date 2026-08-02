a = (1, 2, 0, 45, 89, 45, 34.34)

# len() --> Show the length of the Tupple.
print(len(a))

# Max() --> Show the Max number in tupple.
print(max(a))

# Min() --> Show the minimum no. in Tupple.
print(min(a))

# sum() --> print the sum of of all items in tupple.
print(sum(a))

# sorted() --> Sort The tupple in ascending/Descending order.
print(sorted(a))     # In Ascending order.
print(sorted(a,reverse=True))  # In Descending order.

# Tuple() --> Converts an iterable to a tuple.
p = [1, 2, 4, 56, 65]
print(tuple(p))

# List() --> Converts a tuple to a list.
print(list(a))

# any() --> Return True if atleast one element is True.
print(any(a))

# enumerate() --> Show index-value pairs.
b = ("Apple", "Banana", "Mango")
for index, value in enumerate(b):
    print(index, value)

# count() --> count the repeatition.
print(a.count(45)) 

# index() --> Show the index of item.
b = a.index(2)
print(b)


