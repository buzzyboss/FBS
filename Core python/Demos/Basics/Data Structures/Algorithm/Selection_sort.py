def selectionSort(li):
    size = len(li)
    for i in range(0 , size -1):
        min_ind = i
        for j in range(i+1 ,size):
            if(li[j] < li[min_ind]):
                min_ind = j
        li[i] , li[min_ind] = li[min_ind] , li[i]

li = [56,89,77,91,21,43,78]
print('Before sorting:',li)
selectionSort(li)
print('After sorting:',li)