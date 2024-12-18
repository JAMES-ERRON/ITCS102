name = input("Hi enter your name:")
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
num9_c = num8_c % 1

print("Hi", name,", your deposit amount breakdown in PHP denomination is as follows: ")
print(num1, "- 1000")
print(num2, "- 500")
print(num3, "- 200")
print(num4, "- 100")
print(num5, "- 50")
print(num6, "- 20")
print(num7, "- 10")
print(num8, "- 5")
print(num9, "- 1")