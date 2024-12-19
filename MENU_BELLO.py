import os
import os
import sys
import time

has_account = False
ulit = True
bal = 0

def loading_bar(total_steps=50, step_duration=0.05):
    print("Loading...")
    bar_length = 30 
    for x in range(total_steps + 1):
        percent = (x / total_steps) * 100
        completed_length = int(bar_length * x / total_steps)
        bar = '=' * completed_length + ' ' * (bar_length - completed_length)
        sys.stdout.write(f"\r{bar}] {percent:.1f}%")
        sys.stdout.flush()
        time.sleep(step_duration)
    print("\nFinish!")

def ADDITION():
    global bal
    os.system('cls')
    print("=============== ADDITION ===============")
    num1 = eval(input("Please input a number: "))
    num2 = eval(input("Please input a number: "))
    addition = num1 + num2
    print("==============================")
    print(num1, "+", num2, "=", addition)
    print("The sum of", num1, "and", num2, "is", addition)
    print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def HELLO_WORLD():
    hello_world = input("Would you like to print 'Hello World?' (YES or NO): ")
    if hello_world.lower() == "yes":
        os.system('cls')
        print("Hello World")
        print()
        bla = input("Please enter 'OK' to continue.")
        os.system('cls')

def SUBTRACTION():
    os.system('cls')
    print("=============== SUBTRACTION ===============")
    num1 = eval(input("Please input a number: "))
    num2 = eval(input("Please input a number: "))
    subtraction = num1 - num2
    print("==============================")
    print(num1, "-", num2, "=", subtraction)
    print("The difference between", num1, "and", num2, "is", subtraction)
    print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def MULTIPLICATION():
    os.system('cls')
    print("=============== MULTIPLICATION ===============")
    num1 = eval(input("Please input a number: "))
    num2 = eval(input("Please input a number: "))
    multiplication = num1 * num2
    print("==============================")
    print(num1, "*", num2, "=", multiplication)
    print("The product of", num1, "and", num2, "is", multiplication)
    print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def DIVISION():
    os.system('cls')
    print("=============== DIVISION ===============")
    num1 = eval(input("Please input a number: "))
    num2 = eval(input("Please input a number: "))
    division = num1 / num2
    print("==============================")
    print(num1, "/", num2, "=", division)
    print("The quotient of", num1, "and", num2, "is", division)
    print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def EXPONENT():
    os.system('cls')
    print("=============== EXPONENT ===============")
    num1 = eval(input("Please input a number: "))
    num2 = eval(input("Please input a number: "))
    exponent = num1 ** num2
    print("==============================")
    print(num1, "**", num2, "=", exponent)
    print(num1, "exponent by", num2, "is", exponent)
    print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def REMAINDER():
    os.system('cls')
    print("=============== REMAINDER ===============")
    num1 = eval(input("Please input a number: "))
    num2 = eval(input("Please input a number: "))
    remainder = num1 % num2
    print("==============================")
    print(num1, "%", num2, "=", remainder)
    print("The remainder of", num1, "and", num2, "is", remainder)
    print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def FLOOR_DIVISION():
    os.system('cls')
    print("=============== FLOOR DIVISION ===============")
    num1 = eval(input("Please input a number: "))
    num2 = eval(input("Please input a number: "))
    floor_division = num1 // num2
    print("==============================")
    print(num1, "%", num2, "=", floor_division)
    print("The floor division of", num1, "and", num2, "is", floor_division)
    print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def DENOMINATION():
    os.system('cls')
    print("=============== DENOMINATION ===============")
    cash = eval(input("Please enter the amount:"))

    num1 = cash // 1000
    num1_c = cash % 1000

    num2 = num1_c // 500 
    num2_c = num1_c % 500

    num3 = num2_c // 200
    num3_c = num2_c % 200

    num4 = num3_c // 100
    num4_c = num3_c % 100

    num5 = num4_c // 50
    num5_c = num4_c % 50

    num6 = num5_c // 20
    num6_c = num5_c % 20

    num7 = num6_c // 10
    num7_c = num6_c % 10

    num8 = num7_c // 5
    num8_c = num7_c % 5

    num9 = num8_c // 1

    print("Hi", name, ", your deposit amount breakdown in PHP denomination is as follows: ")
    print(num1, "- 1000")
    print(num2, "- 500")
    print(num3, "- 200")
    print(num4, "- 100")
    print(num5, "- 50")
    print(num6, "- 20")
    print(num7, "- 10")
    print(num8, "- 5")
    print(num9, "- 1")
    print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def AGE_IDENTIFIER():
    os.system('cls')
    print("=============== AGE IDENTIFIER ===============")
    age = eval(input("Enter your age ---> "))
    print("==============================================================================")

    if age >= 1 and age <= 8: 
        print(f"Hello {name}, you are considered as a Toddler because your age is {age}")

    if age >= 9 and age <= 14: 
        print(f"Hello {name}, you are considered as a Preteen because your age is {age}")
    
    if age >= 15 and age <= 18: 
        print(f"Hello {name}, you are considered as a Teenager because your age is {age}")

    if age >= 19 and age <= 27: 
        print(f"Hello {name}, you are considered as a Early Adulthood because your age is {age}")

    if age >= 28 and age <= 44: 
        print(f"Hello {name}, you are considered as a Middle Age because your age is {age}")

    if age >= 45 and age <= 59: 
        print(f"Hello {name}, you are considered as a Post Adulthood because your age is {age}")
    
    if age >= 60 and age <= 150: 
        print(f"Hello {name}, you are considered as a Senior because your age is {age}")
    
    if age >= 150: 
        print("Invalid age")
        print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def MULTIPLICATION_TABLE():
    os.system('cls')
    print("=============== MULTIPLICATION TABLE ===============")
    no = int(input("Enter a number of column: "))

    for x in range (1,no):
        for y in range(1, no+1):
            print(f" |{x}x{y} = {x*y}|", end="")
            print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def GRADES_COMPUTATION():
    os.system('cls')
    print("=============== GRADES COMPUTATION ===============")
    num1 = eval(input("Enter your grade in prelim here: "))
    num2 = eval(input("Enter your grade in midterm here: "))
    num3 = eval(input("Enter your semi-final grade here: "))
    num4 = eval(input("Enter your grade in final here: "))
    num5 = eval(input("Enter your grade in Quiz here: "))
    num6 = eval(input("Enter your grade in project here: "))

    grade = (num1 * .15) + (num2 * .15) + (num3 * .15) + (num4 * .15) + (num5 * .25) + (num6 * .15)

    if grade >= 75 :
        print("          ===============FINAL GRADE===============          ")
        print()
        print(f"Congratulations! You passed the course and your final grade is {grade}")
        print()
    else:
        print("          ===============FINAL GRADE===============          ")
        print()
        print("Sorry, you failed")
        print(f"your final grade is {grade}")
        print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def DIAMOND():
    global bla
    global c
    global e
    global y
    global z
    global a
    os.system('cls')
    print("=============== DIAMOND ===============")
    for x in range(1, 5):
        for y in range(x, 4):
            print(" ", end=" ")
        for z in range(1, x+1):
            print("*", end=" ")
        for a in range(1, x):
            print("*", end=" ")
        print()

    for b in range(1, 6):
        for c in range(b):
            print("  ",end="")
        for e in range(4-b):
            print("*",end=" ")
        for j in range(3-b):
            print("*",end=" ")
        print()
    bla = input("Please enter 'OK' to continue.")

def TRIANGLE():
    os.system('cls')
    print("=============== TRIANGLE ===============")
    print("\nShape 2: Triangle")
    for a in range(0, 7):
        for b in range(0, 7 - a):
            print(" ", end=" ")
        for c in range(1, a * 3 - a):
            print("*", end=" ")
        print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')
 
def SQUARE():
    os.system('cls')
    print("=============== SQUARE ===============")
    for x in range(10):
        for y in range(10):
            print("*", end=" ")
        print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')

def ARROW():
    os.system('cls')
    print("=============== ARROW ===============")
    for x in range(1, 6):
        for y in range(x, 6):
            print(" ", end=" ")
        for z in range(1, x + 1):
            print("*",end=" ")
        for a in range(1, x + 1):
            print("*", end=" ")
        print()

    for b in range(1, 6):
        for c in range(1,x-2):
            print("    ", end=" ")
        for d in range(1,x-2):
            print("*",end=" ")
        print()
    bla = input("Please enter 'OK' to continue.")
    os.system('cls')


def SHAPES():
    while True:
        os.system('cls')
        print("=============== SHAPES ===============")
        print("1. DIAMOND")
        print("2. TRIANGLE")
        print("3. SQUARE")
        print("4. ARROW")
        print("0. BACK TO MAIN MENU")
        choice = input("Select an answer: ")
        if choice == "1":
            DIAMOND()
        elif choice == "2":
            TRIANGLE()
        elif choice == "3":
            SQUARE()
        elif choice == "4":
            ARROW()
        elif choice == "0":
            os.system('cls')
            print("Thank you for using our services.")
            ulit = False
            break

def FACTORIAL():
    os.system('cls')
    print("=============== FACTORIAL ===============")
    num = eval(input("Enter any number: "))
    factorial = 1 

    for x in range(num,0,-1):
        factorial *= x
    print("============================================")
    print(f"The factorial of {num} is: {factorial}")



def OPERATIONS():
    while True:
        os.system('cls')
        print("========== OPERATIONS ==========")
        print("1. ADDITION")
        print("2. SUBTRACTION")
        print("3. MULTIPLICATION")
        print("4. DIVISION")
        print("5. EXPONENT")
        print("6. REMAINDER")
        print("7. FLOOR_DIVISION")
        print("0. BACK TO MAIN MENU")
        choice = input("Select an answer: ")
        if choice == "1":
            ADDITION()
        elif choice == "2":
            SUBTRACTION()
        elif choice == "3":
            MULTIPLICATION()
        elif choice == "4":
            DIVISION()
        elif choice == "5":
            EXPONENT()
        elif choice == "6":
            REMAINDER()
        elif choice == "7":
            FLOOR_DIVISION()
        elif choice == "0":
            break
        else:
            print("Invalid input\n")
            bla = input("Please enter 'OK' to continue.")

while ulit:
    os.system('cls')
    print("Welcome to my Final Project")
    if not has_account:
        os.system('cls')
        print("     <==================== JAMES ERRON'S FINAL PROJECT ====================>     ")
        print("Welcome to JAMES ERRON'S FINAL PROJECT where you can learn absic programming functions in python language")
        print("To continue in this program, you need to create an account ")
        sign_in = input("Would you like to create an account? (YES or NO): ")
        if sign_in.lower() == "yes":
            os.system('cls')
            print("Account Sign Up")
            print()
            name = input("Please enter your name: ")
            password = input("Create your password: ")
            pass_confirm = input("Re-enter your password: ")
            if pass_confirm == password:
                os.system('cls')
                print("Account successfully created")
                loading_bar()
                has_account = True
                bla = input("Please enter 'OK' to continue.")
        elif sign_in.lower() == "no":
            print("Thank you for using our system.")
            ulit = False
            break

    elif has_account:
        while ulit:
            os.system('cls')
            print("Please login your account to access our services.")
            whatname = input("Name: ")
            if whatname == name:
                whatpass = input("Password: ")
                if whatpass == password:
                    while ulit:
                        os.system('cls')
                        print(f"Hi {name}! What would you like to do for today?")
                        print("======================================================")
                        print("1. HELLO WORLD")
                        print("2. OPERATIONS")
                        print("3. DENOMINATION")
                        print("4. AGE IDENTIFIER")
                        print("5. MULTIPLICATION TABLE")
                        print("6. GRADES COMPUTATION")
                        print("7. SHAPES")
                        print("8. FACTORIAL")
                        print("0. EXIT")
                        choice = input("Select an answer: ")
                        if choice == "1":
                            HELLO_WORLD()
                        elif choice == "2":
                            OPERATIONS()
                        elif choice == "3":
                            DENOMINATION()
                        elif choice == "4":
                            AGE_IDENTIFIER()
                        elif choice == "5":
                            MULTIPLICATION_TABLE()
                        elif choice == "6":
                            GRADES_COMPUTATION()
                        elif choice == "7":
                            SHAPES()
                        elif choice == "8":
                            FACTORIAL()
                        elif choice == "0":
                            os.system('cls')
                            print("Thank you for using our services.")
                            ulit = False
                            break
                        else:
                            print("Invalid input")
                            bla = input("Please enter 'OK' to continue.")
                else:
                    os.system('cls')
                    print("Incorrect password.")
                    bla = input("Please enter 'OK' to continue.")
            else:
                os.system('cls')
                print("Account name does not exist.")
                bla = input("Please enter 'OK' to continue.")