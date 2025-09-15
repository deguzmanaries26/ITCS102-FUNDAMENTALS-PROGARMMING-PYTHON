print("ODD Number Summation")
num = 0
for x in range(1, 11, 1):
    number = int(input("Enter a number: "))
    if number % 2 != 0:
        num += number
print("The sum of the odd numbers is", num)