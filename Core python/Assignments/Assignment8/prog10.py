def reverse():
    n = int(input('Enter the number=='))

    rev = 0

    while n > 0: # repeats until n become 0
        r = n % 10       #gets last digit
        rev = rev * 10 + r # adds the digit to rev
        n = n // 10 # removes last digit
    print("Reverse =", rev)

reverse()