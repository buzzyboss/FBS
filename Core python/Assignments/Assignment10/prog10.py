li = [10,20,30,50,10,80,50]

n = int(input('Enter element to remove=='))
new =[]

for i in li:
    if i != n:  #Keep only elements that are not equal to n
        new.append(i) #If i is not 10, add it to new.If i is 10, skip it.
print('Updated list=',new)