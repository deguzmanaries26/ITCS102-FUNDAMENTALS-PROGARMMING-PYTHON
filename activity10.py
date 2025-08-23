name = input("Type your name: ")
isStudent = input("Are you a student? (Yes/No): ").lower()
fare = eval(input("bayad mo: "))
if isStudent == "yes" :
	discount = int((fare*.2)//1)
	new_fare = int(fare - discount)
	print("hello", name,",", discount, "is deducted for the student discount. Your new fare is", new_fare)
else :
	print("sorry", name, "you're not discounted.")