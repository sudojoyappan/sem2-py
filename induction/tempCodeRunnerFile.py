def LHS(n):
    return sum(range([1,n+1]))\

def RHS(n):
    return (n*(n=1))/2

n=int(input("Enter a Number:"))

print("\n base case (n-1):")
for k in range(1,n):
    if LHS(k)==RHS(k) and LHS(k+1)==RHS(k+1):
        print(f"true for k={k} =>True for k+1={k+1}")