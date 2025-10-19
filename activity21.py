isDirty = True 

while isDirty == True:
    laundry = input("Are the clothes still dirty? (yes/no): ").lower()
    if laundry == "yes":
        print("Continuing the cycle...")
        continue
    elif laundry == "no":
        print("Cycle stops")
        break
    else:
        print("Invalid input, please answer with 'yes' or 'no'.")