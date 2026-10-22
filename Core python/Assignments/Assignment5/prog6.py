n = int(input("Enter n: "))
num = 2
count = 0

while count < n:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False

    if prime:
        print(num)
        count += 1

    num += 1