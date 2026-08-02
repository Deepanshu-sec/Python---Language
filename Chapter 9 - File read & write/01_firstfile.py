f = open("first.txt")
data = f.read()
print(data)
f.close()

# the same can be written using "with" statement
with open("first.txt") as f:
    data = f.read()
    print(data)
# file close automatically.