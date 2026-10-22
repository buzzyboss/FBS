def leap():
    year = int(input('Enter the year='))

    if year % 400 == 0 or year % 4 == 0:
        print('Leap year')
    elif year % 100 == 0:
        print('Not leap year')
    
leap()

# 2024