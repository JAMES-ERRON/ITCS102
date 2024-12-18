num1 = eval(input("input a number .: "))
num2 = eval(input("input another number.: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
exponent = num1 ** num2
remainder = num1 % num2
answer = num1 // num2

print("The sum of", num1, "and" , num2, "is", addition)
print("The difference of", num1, "and" , num2, "is", subtraction)
print("The product of", num1, "and" , num2, "is" , multiplication)
print("The quotient of" , num1,"and", num2 , "is", division)
print(num1, "exponent by", num2, "is", exponent)
print("The remainder of", num1, "and", num2, "is", remainder)
print("The floor division of", num1, "and", num2, "is", answer)