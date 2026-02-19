import random
Max_bet=100
Min_bet=1
Max_lines=3
Min_lines=1

def deposit():
    while True:
        amount= input("what would you like to  deposit? $")
        if amount.isdigit():
            amount= int(amount)
            if amount>0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("please enter a number.")
    
    return amount

def lines():
    while True:
        lines= input(f"how many lines would you like to bet on?{Min_lines}-{Max_lines} ")
        if lines.isdigit():
            lines= int(lines)
            if Max_lines>=lines<=Min_lines:
                break
            else:
                print(f"amount must be or btw {Min_lines}-{Min_lines} ")
        else:
            print("please enter a number.")
    
    return lines 

def main(): 
    balance=deposit()
    bet= lines()

main()