def mutli(number):
    i=0
    while i<=10:
     result= number* i
     print(f"{number}X{i}={result}")
     i+=1


number= int(input("Enter a no. "))
mutli(number)