for i in range(1 , 5):
    for j in range(i):
        if j == 0 or j == i -1:
            print('1',end =' ')
        else:
            print(i - 1,end=' ')
    print()

