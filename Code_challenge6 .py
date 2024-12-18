name = input("Please input your name ---> ")
age = eval(input("Enter your age ---> "))

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