# Palindrome Checker

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
