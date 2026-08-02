# readlines()
f = open("first.txt")
data = f.readlines()
print(data,type(data))

f = open("first.txt")
data = f.readline()
print(data,type(data))


f.close()