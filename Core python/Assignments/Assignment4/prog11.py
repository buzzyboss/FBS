n = int(input('Enter the number=='))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    fact = 1
    for i in range( 1 , digit+1):
        fact = fact * i

    sum += fact
    n = n // 10
if sum == temp:
    print('Strong number')
else:
    print('not Strog number')