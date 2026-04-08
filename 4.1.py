x=int(input("Enter number of elements of fibonacci series:"))
lst=[0,1]
for i in range(2,x):
    lst.append(lst[i-1]+lst[i-2])

print(lst)