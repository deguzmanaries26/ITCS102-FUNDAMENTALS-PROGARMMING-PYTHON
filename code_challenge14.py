name = input("Hello! What is your name? ")
print("ODD number compiler, type '0' to terminate")
Odd = True
number = 0
odd_number = []
while Odd == True:
    num = int(input("Type a number: "))
    if num == 0:
        print("Program terminated.")
        break
    elif num % 2 == 0:
        print("Even number detected.")
        continue
    elif num % 2 == 1:
        print("Odd number detected.")
        number += num
        odd_number.append(num)
        continue
    else: 
        print("Invalid input, program terminated.")
        break
print(f"Hello {name}, The sum of all ODD numbers you have entered is {number}.")
print(f"All the ODD numbers you have entered are {odd_number}.")
