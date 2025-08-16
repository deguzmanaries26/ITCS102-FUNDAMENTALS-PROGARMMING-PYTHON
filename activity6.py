x1 = eval(input("Input a number:"))
x2 = eval(input("Input another number:"))

s = x1 + x2
d = x1 - x2
p = x1 * x2
q = x1 / x2 

solution = ((x1 / x2)*100-5)//300
print("\nThe sum of" ,x1, "and" ,x2, "is" ,s)
print("The difference of" ,x1, "and" ,x2, "is" ,d)
print("The product of" ,x1, "and" ,x2, "is" ,p)
print("The quotient of" ,x1, "and" ,x2, "is" ,q)
print(x2, "exponent by" ,x2, "is" ,x1**x2)
print("The remainder of" ,x1, "and" ,x2, "is" ,x1 % x2)
print("The floordivision of" ,x1, "and" ,x2, "is" ,x1 // x2)
