# WAP which finds out whether a given name is present in a list or not.

l = ["Deepanshu", "Harvey","Mike","Louis","Jon"]

name = input("Enter the name : ")

if(name in l):
    print("Name is present in list:")
else:
    print("Name is not present in list:")