n = int(input('Enter n='))
x = int(input('Enter x '))
sum = 0
for i in range(1 , n+1):
    term = (x ** i) / (2 * i -1)

    if i % 2 == 0:
        sum = sum -term
    else:
        sum = sum +term
print(sum) 