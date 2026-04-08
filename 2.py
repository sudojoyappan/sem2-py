def power(base,exp):
    if exp==0:
        return 1
    elif exp>0:
        return base*power(base,exp-1)
    else:                                   
        return 1/(power(base,-exp))
    
base=int(input("Enter a base number:"))
exp=int(input("Enter a exponential value:"))
print("The Exponential value is:",power(base,exp))