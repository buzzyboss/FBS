def fact(n):
    if n == 1 or n == 0:
        return 1

    
    return n * fact(n-1)

n = int(input('Enter the number= '))
print('factorial= ',fact(n))


# 1. Accept a number from the user.
# 2. If n == 0 or n == 1, return 1.
# 3. Otherwise, multiply n by fact(n - 1).
# 4. Print the result.