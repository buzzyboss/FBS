#Python Program to Sort the List According to the Second Element in Sublist

li =[[2,5],[1,8],[7,1],[9,2]]

li.sort(key=lambda x : x[1])

print('sorted list=',li)

# key=lambda x: x[1] tells Python to sort according to the second element of each sublist.
# x[1] means the second element because Python indexing starts from 0.