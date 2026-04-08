def conjunction(a,b):
    return(a and b)
def disjunction(a,b):
    return(a or b)
def conditional(a,b):
    return disjunction(not a,b)
def biconditional(a,b):
    return conjunction(conditional(a,b),conditional(b,a))


def all(list):
    c=0
    for i in list:
        if i:
            c+=1
    if c==len(list):
        return True
    else:
        return False
def any(list):
    for i in list:
        if i:
            return True
        


values=[True,False]

#((p->q)^(q->r))->(p->r)
l=[]
print("((p->q)^(q->r))->(p->r)")
print("p \t q \t r \t p->q \t q->r \t p->r \t ((p->q)^(q->r))->(p->r)")
for p in values:
    for q in values:
        for r in values:
            a=conditional(p,q)
            b=conditional(q,r)
            c=conditional(p,r)
            d=conjunction(a,b)
            l.append(conditional(d,c))
            print(f"{p} \t {q} \t {r} \t {a} \t {b} \t {c} \t {conditional(d,c)}")


if all(l):
    print("TAUTOLOGY")
elif not any(l):
    print("CONTRADICTION")
else:
    print("CONTINGENCY")