#with passing parameter and with returning value
def addition(num1 ,num2):
    result = num1 + num2
    return result

num1 = int(input('Enter the num1:'))
num2 = int(input('Enter the num2:'))

    
res = addition(num1 , num2)
print('Result = ',res)