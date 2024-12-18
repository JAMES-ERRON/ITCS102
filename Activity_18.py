# #This function is for calculating factorial

# def factorial(number):
#     """THIS FUNCTION IS FOR CALCULATING FACTORIAL, JUST PUT THE NUMBER INSIDE THE PARENTHESIS"""
#     fact = 1
#     for x in range(number, 0, -1):
#         fact *= x
#         print(x)
#     return fact

# #help(factorial)
# #help(print)
# #help(input)
# #help(help)

num = eval(input("Enter any number: "))
factorial = 1 

for x in range(num,0,-1):
    factorial *= x
print(f"The factorial of {num} is {factorial}")
