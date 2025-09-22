print("\t\t   *")
for i in range(1,11,1):
    for z in range(10,i,-1):
        print(" ", end=" ")
    for x in range(0,i,1):
        print("*", end=' ')
    for y in range(0,i,1):
        print("*", end=" ")
    print()