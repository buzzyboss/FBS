def reverse( n , rev):
    if n == 0:
        return rev

    digit = n % 10
    rev = rev * 10 + digit

    return reverse(n // 10,rev)

n = int(input('Enter the number='))
print('Reversed = ',reverse(n , 0))

# - n % 10 extracts the last digit.
# - rev * 10 + digit adds the digit to the reversed number.
# - n // 10 removes the last digit.
# - return reverse(n // 10, rev) calls the function again.
# - if n == 0 stops the recursion.
# - reverse(n, 0) starts with the reversed number set to 0.