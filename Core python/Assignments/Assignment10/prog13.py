li = [1,2,3,4,5,6,7,8,9,10]

new =[]

for i in li:
    if i % 2 != 0:
        new.append(i)
print('List after removing even numbers=',new)
