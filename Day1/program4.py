#Q4. Write a program that takes an integer input from the user and prints whether the number is positive, negative, or zero.

num = int(input("Enter an integer: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")