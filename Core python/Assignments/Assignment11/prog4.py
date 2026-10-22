li =[1,2,3,4,2,3,6,54,2,8,9,5,11]

for i in range(len(li)):
    for j in range(len(li)-1):
        if(li[j] > li[j+1]):
            temp=li[j]
            li[j]=li[j+1]
            li[j+1]=temp

print('sorted list=',li)
print('second largest number is =',li[-2])
