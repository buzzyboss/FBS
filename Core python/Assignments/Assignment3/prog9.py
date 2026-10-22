python = int(input('Enter marks =='))
english = int(input('Enter marks =='))
marathi = int(input('Enter marks =='))
maths = int(input('Enter marks =='))
physics = int(input('Enter marks =='))

grade = python + english + marathi + maths + physics
print('total marks=',grade)

percentage = grade /5
print('percentage=',percentage)

if percentage > 90:
    print('####### First class. ########')

elif percentage >70 and percentage <90:
    print('#####  second class  ####')

elif percentage > 50 and percentage < 70:
    print('##### third class #####')

elif percentage > 35 and percentage <50:
     print('##### fourth class #####')

else:
    print('Failled broooooooo')