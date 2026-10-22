def fibo():
    n = int(input('Enter n =='))
    a = 1
    b = 1

    for i in range(n):
        print(a)
        c = a+b
        a = b
        b = c
fibo()