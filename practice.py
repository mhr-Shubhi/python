class Expense:
    def __init__(self,amount,category,note):
        self.amount = amount
        self.category = category
        self.note= note

expense = []

while True:
    user_input= input("What would you like to do? A)add b)view c)total d)category e)exit").lower()

    if user_input == "add":
        print()
    elif user_input == "view":
        print
    elif user_input=="total":
        print()
    elif user_input=="category":
        print()
    elif user_input=="exit":
        break     
    
