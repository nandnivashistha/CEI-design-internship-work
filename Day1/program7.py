#Q7. Create a program that prints the multiplication table of a given number using a while loop.

num = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(num, 'x', i, '=', num * i)
    i += 1