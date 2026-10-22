'''Write a program to check if person is eligible to marry or not (male age >=21 and
female age>=18)'''

gender = input('Enter the gender===')
age = int(input('Enter the age==='))

if gender == 'Female' and age >=18:
    print('female is eligible for marriage')
elif gender == 'Male' and age >=21:
    print('Male is eligible for marriage')
else:
    print('Padhai karo beta ')