#1.write a function to print factor of a given number
def print_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i,end=" ")

num = int(input("Enter a number: "))
print("Factors of", num, "are:")
print_factors(num)