n = int(input('Enter number of students=='))

total_percentage = 0
for i in range(n):
    total = 0
    maths = int(input('Enter marks of maths='))
    science = int(input('Enter marks of science='))
    geography = int(input('Enter marks of geograpy='))
    java = int(input('Enter marks of java='))
    Linear_algebra = int(input('Enter the marks of linear algebra='))

    total = maths + science + geography + java + Linear_algebra

    percentage = total / 5
    print('percentage =',percentage)

    total_percentage +=percentage

average = total_percentage/n
print('Average percentage =' , average)