#Q2. Create a program that takes user input to add multiple elements to an array, then prints the final array

array = []

n = int(input("number of elements in a array? "))

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    array.append(element)

print("Array:", array)
