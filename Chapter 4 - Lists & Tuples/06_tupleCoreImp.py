# Concatenation = add two or more subjects.

tuple1 = (1, 2 , 3)
tuple2 = (4, 5 , 6)

concatenated = tuple1 + tuple2
print(concatenated)

# Repetition --> Repeat the tuple.

tuple1 = (1, 2, 3)
repeated = tuple1 * 3   # Output -> (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(repeated)

# Slicing 
My_tuple = (1, 2, 3, 4, "Deepanshu", "Harvey")
sliced = My_tuple[0:5]    # like string (Give a new tuple).
print(sliced)

# Membership
tuple = (1, 2, 3, 4, 5)
print(2 in tuple)    # Output --> true
print(10 in tuple)   # Output --> False


# unpacking
tuple = (1, 2, 3)  # assign 1,2,3 in a,b,c .
a, b, c = tuple
print(a, b, c)
