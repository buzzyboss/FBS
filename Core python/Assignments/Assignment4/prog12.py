n = int(input('Enter number=='))

temp = n
sum = 0
count = 0

while n > 0:
    count += 1
    n = n//10

n = temp

while n > 0:
    digit = n % 10
    sum += digit**count
    n = n // 10

if sum == temp:
    print('armstrong')
else:
    print('not armstrong')
