def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
    


x=int(input("Enter number to check fibonacci series numbner at that index:"))
for i in range(x):
    print(fibo(i))