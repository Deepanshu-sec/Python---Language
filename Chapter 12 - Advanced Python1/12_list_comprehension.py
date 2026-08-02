mylist = [1,2,3,4,5,6]

# squaredlist = []
# for item in mylist:             # --> return a list with element's square.
#     squaredlist.append(item*item)
# print(squaredlist)

            # By List Comprehension

squaredlist = [i*i for i in mylist]
print(squaredlist)