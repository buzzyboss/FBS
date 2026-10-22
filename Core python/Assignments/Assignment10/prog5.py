li = [10,20,60,99,78,60,9,3]

n = int(input('Enter the number = '))

count = 0

for i in li:
    if i == n:
        count += 1

if count > 0:
    print('Element present ')
    print('Present ' , count , 'times')
else:
    print('Element is not present ')