a = {
    "Deepanshu" : 10,
    "Harvey" : 10,
    "Jon Snow" : 9,
    "Louis Litt": 8,
    0 : "Skyler White"
}

# len() --> Show the number of key-value pairs.
print(len(a))

# items() --> Show the items in tuple's form.
print(a.items())

# keys() --> Show the keys in tuple's form.
print(a.keys())

# values() --> Show the values in dictionary.
print(a.values())

# update() --> update/change/add items in dictionary.
a.update({"Jon Snow":10,"Pearson" : 10})
print(a)

# get() --> Key ki value safely return karta h agar key exist na kre to none dega na kin error.
print(a.get("Harvey"))
print(a.get("Harvey2"))  # --> Return None.
# print(a["Harvey2"])     # --> Return Error.

# pop() --> remove the key and value.
a.pop(0)
print(a)

# popitem() --> Delete Last insert dictionary value.
a.popitem()
print(a) 

a = {}
print(type(a))