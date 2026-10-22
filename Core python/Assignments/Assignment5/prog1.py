correct_userid = 'Vishu'
correct_password = 'reva'

for i in range(3):
    userid = input('Enter the userid')
    password = input('Enter the password')

    if userid == correct_userid and password==correct_password:
        print('login successfulllll')
        break
    else:
        print('Invalid user id or password')

else:
    print('3 attempts completed.program terminated.')