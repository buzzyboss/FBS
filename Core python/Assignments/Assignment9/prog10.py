def reverse(n,rev):
    if n == 0:
        return rev

    
    digit = n % 10
    rev = rev * 10 + digit

    return reverse(n // 10, rev)


n = int(input('Enter n =='))
print('REVersed== ',reverse(n,0))

# n % 10 → gets the last digit.
# n // 10 → removes the last digit.
# rev * 10 + digit → builds the reversed number.
# return reverse(...) → calls the function again.