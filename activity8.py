balance = 1000000
amount = 0

amount = int(input("Enter the amount to withdraw:"))
print(balance >= amount)
if balance >= amount:
	newbal = balance - amount
	print("withdrawal Granted! \nYour new balance is", newbal)
elif balance <= amount:
	print("You currently don't have enough balance in your account.")