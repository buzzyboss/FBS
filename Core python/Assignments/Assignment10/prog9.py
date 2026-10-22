li = [10,20,99,45,34,67,112,453,876,145]

even =[]
odd =[]

for i in li:
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)
print('Even list =',even)
print('Odd list =',odd)
