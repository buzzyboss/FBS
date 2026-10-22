"""Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)"""

import random
userid = input('Enter user id pls ====')
password = input('Enter password pls ===')

if userid == 'admin' and password == '1234':
    print('userid and password is correct')
else:
    print('userid and password is not correct')


num = random.randint(1000, 9999)
print(num)
num1 = int(input('Enter the number given =='))

if num == num1:
    print('Successssssss bc')
else:
    print('Failed laudeeee')