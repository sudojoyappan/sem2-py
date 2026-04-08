def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("Enter a Number:"))
if n<0:
    print("Number is negative,Factorial doesnt exist")
else:
    print(factorial(n)) 
