for i in range(1,6):
    for j in range(1,6):
        print('*', end=' ')
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print('*', end=' ')
    print()

for i in range(1,7):
    for j in range(i+1,7):
        print('*', end=' ')
    print()


#     #or

for i in range(1,7):
    for j in range(1,7-i):
        print(j, end=' ')
    print()


for i in range(1,7):
    for j in range(6-i,0,-1):
        print(j, end=' ')
    print()

