sum = 0 
odd = 0 
even = 0 
for x in range(1, 11):
    number = eval(input(f"Enter a number{x}:   "))
    sum += number
    if number % 2 == 0:
        even += number
    else:
        odd =+ number
print(f" The sum of all the number is: {sum}")
print(f" The sum of all EVEN number is = {even}")
print(f" The sum of all ODD number is = {odd}")
