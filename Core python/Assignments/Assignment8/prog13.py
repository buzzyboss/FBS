def arm():
    n = int(input('Enter n ='))
    temp = n
    sum = 0

    while n > 0:
        r = n % 10
        sum = sum + (r**3)
        n = n // 10

    if temp == sum:
        print('Armstrong')
    else:
        print('not Armstrong')
arm()

# 153