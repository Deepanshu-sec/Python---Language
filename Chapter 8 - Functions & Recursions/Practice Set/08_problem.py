# write a function to remove a given word from a list ad strip it at the same time.
def func(x,word):
    n = []
    for item in x:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Deepanshu","Harvey Specter","Himanshu","Devanshu"]

print(func(l,"hu"))
