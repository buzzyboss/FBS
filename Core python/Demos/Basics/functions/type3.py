#without passing parameter and with returning value
def addition():
    num1 = int(input('Enter the num1:'))
    num2 = int(input('Enter the num2:'))

    result = num1 + num2
    return result

res = addition()
print('Result = ',res)