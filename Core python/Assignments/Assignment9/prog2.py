def arm(n , p):
    if n == 0:
        return 0
    digit = n % 10
    return digit ** p + arm(n // 10 , p)

num = int(input('Enter number=='))
p = len(str(num))

if num == arm(num ,p):
    print('Armstrong')
else:
    print('Not Armstrong')