print("This program calculates the factorial of a number.")
number = int(input("Enter a number: "))
num = 1 
for x in range(number, 1, -1):
    num *= x
print("The factorial of", number, "is", num) 