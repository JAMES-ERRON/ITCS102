#CONDITIONS
#all product prices would be be taxed 12.3% added to the product price 
#if the untaxed price is more than 4,000 a discount of 3.8% of the untaxed product price would beb applied. 
#if age is more than 60 and not higher than 150, a senior discount is 12.3%.
#notify the custumer of his change 

#TARGET OUTPUT
#ENTER YOUR NAME:
#DID YOU PURCHASE A GROCERY TODAY? (YES,NO)
#WHAT DID YOU PURCHASE:
#ITEM PRTCE:
#AGE:
#PAYMENT:

Tax_rate = 0.123
Discount_rate = 0.038
Senior_discount_rate = 0.123

name = input("Enter your name:")
answer = input("Did you purchase a grocery today? (Yes/No):")
if answer.lower() == "yes":
     Item = input("What item did you purchase:")
     Item_price = float(input("What was the price of the item:"))
     print()
     taxed_price = Item_price + Item_price * Tax_rate
     print(f"A tax of {Tax_rate * 100}% is applied. The new price (with tax) is {round(taxed_price, 2)}")
    
     #ask age for a senior discount
     age = eval(input("What is your current age:"))

     if Item_price >= 4000:
          discount = Item_price * Discount_rate
          discounted_price = Item_price - discount
          print(f"Since you purchased more than Php 4000, a discount of {Discount_rate * 100}% is applied to the original price.")
          # Update final price with discount
          final_price = discounted_price + (discounted_price * Tax_rate)
          print(f"Final price (with tax after discount) is {round(final_price, 2)}")
          print()

     #discount for senior citizens
     if age >= 60 and age <= 150:
           senior_discount = Item_price * Senior_discount_rate
           Item_price -= senior_discount
           print(f"You are eligible for the {Senior_discount_rate * 100}% senior discount.")
     else:
          print("No senior discount!")

      # Final price after all conditions
     print(f"Total amount to pay is {round(Item_price, 2)}")
     print()
     # Ask for payment and calculate change
     payment = float(input("Please enter your payment amount: "))
     change = payment - Item_price

      # If payment is insufficient
     if change < 0:
        print("Insufficient payment.")
        payment = float(input("Enter payment amount: "))
        change = payment - Item_price
        print(f"Change: {round(change, 2)}")
     else:
        print(f"Change: {round(change, 2)}")
     
else:
    print("OK! see you next time")
