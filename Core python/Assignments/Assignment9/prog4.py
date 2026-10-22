def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

n = int(input('Enter the number=='))
print('sum =',sum(n))

# if n == 0 → stopping condition.
# return 0 → returns zero when recursion stops.
# return n + sum(n - 1) → adds the current number and calls the function again.