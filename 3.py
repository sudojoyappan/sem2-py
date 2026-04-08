def hcf(max,min):
    if min==0:
        return max
    else:
        return hcf(min,max%min)
    

max = int(input("Enter first number: "))
min = int(input("Enter second number: "))

print(f"HCF of {max} and {min} is: {hcf(max, min)}")