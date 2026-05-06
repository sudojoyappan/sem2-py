def trans(n,relations):
    A=[[0]*n for _ in range(n)]

    for a,b in relations:
        A[a-1][b-1]=1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if A[i][k] and A[k][j]:
                        A[i][j]=1

    return A

relations=[]
n=int(input("Enter number of elements:"))
m=int(input("Enter number of pairs:"))

print("Enter pairs(a,b)")

for _ in range(m):
    a,b=map(int,input().split())
    relations.append((a,b))
    results=trans(n,relations)

    print("Transitive Closure")
    for row in results:
        print(*row)

