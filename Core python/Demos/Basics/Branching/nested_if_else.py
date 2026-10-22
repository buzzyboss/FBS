gender = input('Enter gender(F/M):')
age = int(input('Enter age:'))


if(gender == 'M'):
    if(age >=21):
        print('Male is eligible for marriage')

    else:
        print('Pehle kama le bhadwee')
else: 
    if(age>=18 and gender == 'F'):
        print('Girl is eligible for marriage')
    else:
        print('Pehle Padhai karlo bhen ki lawdiii')