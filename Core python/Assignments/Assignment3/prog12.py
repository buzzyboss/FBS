num = int(input("Enter a 3 digit number: "))

first = num // 100
last = num % 10

if first == last:
    print("Palindrome")
else:
    print("Not Palindrome")