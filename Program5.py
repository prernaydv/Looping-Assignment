# Write a Python program to find the factorial of a number using a for loop.
number = int(input("Enter the number : "))

factorial = 1
for i in range(1, number +1):
    factorial *= i
print(f"The factorial of {number} is : {factorial}" )    
