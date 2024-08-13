##_____projectAtmSimulation( using nested if-else)_____

name=input("Plz enter your name:")
print("Hello",name,"!")

message="""
How may I help you sir.

Please Select any of the option,
Type 1 >>>>> CHECK  BALANCE
Type 2 >>>>> DEPOSIT AMOUNT
Type 3 >>>>> WITHDRAWL AMOUNT  
"""
print(message)
task=int(input("Plz enter your option : "))
available_amount=5000

if(task>=1 and task<=3):
    print("Welcome to you in virtual bank program")

    if(task==1):
        #check  balance program
        print("Your available amount is : ",available_amount,"INR")

    elif(task==2):
        #deposit amount
        deposit_amount=int(input("Plz enter deposit amount : "))
        if(deposit_amount>0):
            available_amount+=deposit_amount
            print("You have successfully deposit amount : ",deposit_amount)
            print("Now your available amount is : ",available_amount,"INR")
        else:
            print("Plz enter valid amount !")

    else:
        #withdrawl amount
        withdrawl_amount=int(input("Plz enter the withdrawl amount : "))
        if(withdrawl_amount<=available_amount):
             available_amount-=withdrawl_amount
             print("You have successfully withdraw amount : ",withdrawl_amount)
             print("Now your available amount is : ",available_amount,"INR")
            
        else:
            print("Insufficient Balance in your account !")
            print("Your available amount is : ",available_amount,"INR")

else:
    print("Plz choose valid option between 1 to 3 !")        