def powerr(m,n):
    if n == 0:
        return 1

    return m * powerr(m , n-1)

m = int(input('Ennter M =='))
n = int(input('Enter N =='))

print('Answer =' , powerr(m,n))