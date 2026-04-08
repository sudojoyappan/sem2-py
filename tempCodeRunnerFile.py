#~(pVq)<->(~p^~q)
def conjunction(a,b):
    return (a and b)
def disjunction(a,b):
    return (a or b)
def conditional(a,b):
    return disjunction(not a,b)
def biconditional(a,b):
    return conjunction(conditional(a,b),conditional(b,a))


print("p \t q \t ~(pVq) \t (~p^~q) \t ~(pVq)<->(~p^~q)")
values=[True,False]
for p in values:
    for q in values:
        a=not disjunction(p,q)
        b=conjunction(not p,not q)
        c=biconditional(a,b)
        print(f"{p}\t{q}\t{a}\t{b}\t{c}")