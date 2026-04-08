values=[True,False]
print("p \t q \t p V q")
# for p in values:
#     for q in values:
#         print(f"{p} \t {q} \t {p or q}")

# for p in values:                                                  #p or q and not(p and q)
#     for q in values:
#         print(f"{p} \t {q} \t {p and q}")


for p in values:
    for q in values:
        a=not p or q
        b=not q or p
        print(f"{p} \t {q} \t {a and b}")


for p in values:
    for q in values:
        a=not p or q
        b=not q or p
        c=a and b
        print(f"{p} \t {q} \t {not c}")


        #p or q and not(p and q)