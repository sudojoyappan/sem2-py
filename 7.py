def conjunction(a,b):
    return (a and b)

def disjunction(a,b):
    return (a or b)

def conditional(a,b):
    return disjunction(not a,b)

def biconditional(a,b):
    return conjunction(conditional(a,b),conditional(b,a))

def XOR(a,b):
    return not biconditional(a,b)


values=[True,False]

print("BICONDITIONAL")
print("p \t q \t p <--> q")
for p in values:
    for q in values:
        print(f"{p} \t {q} \t {biconditional(p,q)}")

print("XOR")
print("p \t q \t p XOR q")
for p in values:
    for q in values:
        print(f"{p} \t {q} \t {XOR(p,q)}")
        