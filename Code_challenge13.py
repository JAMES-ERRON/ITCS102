ituloy = True 
sum = 0
while ituloy == True :
    num = eval(input("Please enter a number---> "))

    if num == 0:
        print("LOOP HAS ENDED!")
        print(f"The sum of all numbers given are: {sum}")
        break 
        ituloy = False 
    else:
        sum += num
        continue