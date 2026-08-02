# sort() --> Update the List {Ascending, Descending}.
a = [1,6,7,2,21,15]
a.sort()              # --> In Ascending order.
print(a)

a.sort(reverse=True)  # --> In Descending order.
print(a)


# reverse() --> Reverse the list.
a.reverse()
print(a)


# append() --> Add element at the end of the list.
a.append("Deepanshu")
print(a)


# insert(3,8) --> This will add 8 at 3 index.
a.insert(3,8)
print(a)


# pop(2) --> Will delete element at index 2 and return its value.
a.pop(2)            # --> 2 index pe jo bhi h use delete kar dega.
print(a.pop(2))     # --> Ab jo 2 index pe hoga use Dikhayega + delete kar dega.
print(a)            # Ab jo list banegi use print kar dega.


# remove(21) --> Will remove 21 from the list.
a.remove(21)
print(a)

# count() --> print the occurrences(Repeatition) of item.
b = a.count(7)
print(b)


# index() --> Print the index of the item.
c = a.index(15)
print(c)     # Or --> print(a.index(15)) 


# extend([]) --> Add the multiple items at the end.
a.extend([4,5])
print(a)


# clear() --> Clear all the items in list.
print(a.clear())

