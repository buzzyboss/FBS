# Find the sum of the series \(1!+2!+3!+\cdots+n!\) using recursive functions.

# - if n == 1: This is the stopping condition.
# - return 1: Factorial of 1 is 1.
# - return n * fact(n - 1): Calls the same function again to calculate the factorial.
# For example, fact(3) = \(3 \times 2 \times 1 = 6\).

# if n == 0: Stops the recursion.
# return 0: Nothing more is added.
# return fact(n) + series(n - 1): Adds the current factorial to the sum of the previous factorials.

# fact() calculates factorial, while series() adds all the factorials. Both functions call themselves, so this is recursion.


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def sum(n):
    if n == 0:
        return 0
    return sum(n-1) + fact(n)

n = int(input('Enter n =='))
print('suum = ',sum(n))