values=[True,False]



#AND
print("AND")
print("p \t q \t p Λ q")
for p in values:
    for q in values:
        r1=p and q
        print(f"{p} \t {q} \t {r1}")

#OR
print("OR")
print("p \t q \t p V q")
for p in values:
    for q in values:
        r2=p or q
        print(f"{p} \t {q} \t {r2}")

#XOR
print("XOR")
print("p \t q \t p XOR q")
for p in values:
    for q in values:
        a=not p or q
        b=not q or p
        c=a and b
        print(f"{p} \t {q} \t {not c}")

#IMPLICATION/CONDITIONAL
print("CONDITIONAL")
print("p \t q \t p --> q")
for p in values:
    for q in values:
        r3=not p or q
        print(f"{p} \t {q} \t {r3}")

#BICONDITIONAL
print("BICONDITIONAL")
print("p \t q \t p <--> q")
for p in values:
    for q in values:
        a=not p or q
        b=not q or p
        c=a and b
        print(f"{p} \t {q} \t {c}")


print("p \t q \t not q \t p or not q \t p and q \t not(p or not q) or (p and q)")
for p in values:
    for q in values:
        a=not q
        b=p or a
        c=p and q
        d=not b or c
        print(f"{p} \t {q} \t {a} \t {b} \t\t {c} \t\t {d}")