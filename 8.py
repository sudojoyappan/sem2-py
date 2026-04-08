#((p->q)^(q->r))->(p->r)
#~(pVq)<->(~p^~q)
#(p^q^(q->r))V(p->r)

def conjunction(a,b):
    return(a and b)
def disjunction(a,b):
    return(a or b)
def conditional(a,b):
    return disjunction(not a,b)
def biconditional(a,b):
    return conjunction(conditional(a,b),conditional(b,a))

values=[True,False]

print("((p->q)^(q->r))->(p->r)")
print("p \t q \t r \t p->q \t q->r \t p->r \t (p->q)^(q->r) \t ((p->q)^(q->r))->(p->r)")
for p in values:
    for q in values:
        for r in values:
            a=conditional(p,q)
            b=conditional(q,r)
            c=conditional(p,r)
            d=conjunction(a,b)
            print(f"{p} \t {q} \t {r} \t {a} \t {b} \t {c} \t {d} \t {conditional(d,c)}")


print("\n\n")


#~(pVq)<->(~p^~q)

print("p \t q \t ~(pVq) \t (~p^~q) \t ~(pVq)<->(~p^~q)")
for p in values:
    for q in values:
        a=disjunction(not p ,q)
        b=conjunction(not p,not q)
        c=biconditional(a,b)
        print(f"{p} \t {q} \t {a} \t {b} \t {c}")

print("\n\n")