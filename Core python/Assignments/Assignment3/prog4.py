a = int(input('Enter the 1st angle of the triangle'))
b = int(input('Enter the 2nd angle of the triangle'))
c = int(input('Enter the 3rd angle of the triangle'))

if a+b > c and b+c >a and a +c >b:
    print('The triangle is valid')
else:
    print('The triangle is not valid')