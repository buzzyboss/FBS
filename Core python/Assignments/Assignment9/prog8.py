def primi(n,i):    #n is the number entered by the user.
# i is the number we use to check divisibility.
    if n < 2:
        return False
# Numbers less than 2 are not prime.
# return False means the number is not prime.
    if i == n:
        return True
# If i becomes equal to n, no smaller number divided it exactly.
# So, the number is prime.
    if n % i == 0:
        return False
    return primi(n , i+1)  #This is called recursion.
# If the remainder is 0, n is divisible by i.
# Therefore, the number is not prime
n = int(input('Enter the n ='))

if primi(n , 2): #Starts checking from i = 2.
    print('prime')
else:
    print('not prime')
