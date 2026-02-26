def odd_even(number):
    if number%2==0:
        print("Even")
    
    else:
        print("Odd")
    return number

number=input("Enter a no. ")
try:
     number=int(number)
     odd_even(number)
except ValueError:
     print("Enter a no.")