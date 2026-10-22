li = [10,80,56,22,76,88,25,90,100,80000]

max = li[0]

for ind in range(1 , len(li)):
    if(li[ind] > max):
        max =li[ind]
print('Max :',max)