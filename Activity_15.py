import os


ipagpatuloy = True 
numeric = 0 
while ipagpatuloy == True :
    val = input("Do you want to print more triangles (yes or no ) / ---> ")

    if val.lower() == "no":
        print("LOOP HAS ENDED")
        break 
        ipagpatuloy = False 

    elif val.lower() == "yes":
        os.system('cls')
        numeric += 1
        for j in range(1, 6):
            for e in range(1, numeric + 1):
                for l in range(1,j + 1):
                    print("*", end=" ")
                for o in range(6, j, -1):
                    print(" ", end=" ")
                print(end=" ")
            print()
        continue
    else:
        print("INVALID SELECTION")
        print("PLEASE TYPE Yes or NO ")