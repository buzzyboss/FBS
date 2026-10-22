a = int(input('Enter the 1st angle of the triangle'))
b = int(input('Enter the 2nd angle of the triangle'))
c = int(input('Enter the 3rd angle of the triangle'))

if a == b and b == c and a == c:
    print('Triangle is equilateral')

elif a == b or b == c or a == c:
    print('Triangle is isosceles')

elif a != b and b != c and a != c:
    print('Triangle is scelene')