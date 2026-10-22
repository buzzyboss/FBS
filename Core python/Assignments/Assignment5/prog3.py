n = int(input('Enter the number of passengers='))
tcost = int(input('Enter the ticket cost per person='))

total = 0

for i in range(n):
    age = int(input('Enter age of the person'))

    if age <12:
        amount=tcost * 70 / 100
    elif age >59:
        amount=tcost * 50 / 100
    else:
        amount = tcost
    total += amount
print('Total amount =',total)