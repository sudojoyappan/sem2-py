values=[True,False]

def conjunction(a,b):
    return a and b
def disjunction(a,b):
    return a or b
def conditional(a,b):
    return disjunction(not a,b)
def biconditional(a,b):
    return conjunction(conditional(a,b),conditional(b,a))
def XOR(a,b):
    return not biconditional(a,b)


def all(l):
    c=0
    for i in l:
        if i:
            c+=1
    if c==len(l):
        return True
    else:
        return False
    
def any(l):
    for i in l:
        if i:
            return True



l=[]
print("((p->q)^(q->r))->(p->r)")
print("p \tq \tr \tp->r \tq->r \tp->r \t((p->q)^(q->r))->(p->r)")
for p in values:
    for q in values:
        for r in values:
            a=conditional(p,q)
            b=conditional(q,r)
            c=conditional(p,r)
            d=conjunction(a,b)
            l.append(conditional(d,c))
            print(f"{p} \t{q} \t{r} \t{a} \t{b} \t{c} \t{conditional(d,c)}")


if all(l):
    print("Tautology")
elif not any(l):
    print("Contradiction")
else:
    print("Contingency")