ft = float(input('Enter the distance in feet ==='))
inch = float(input('Enter the distance in inches ==='))
a = ft * 12 
total_inch = a + inch
cm = total_inch * 2.54
mtr = cm /100

print(f'the distance in cm is {cm} and the distance in mtr is {mtr} . ' )
