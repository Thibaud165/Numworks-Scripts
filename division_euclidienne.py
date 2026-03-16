def de(a, b):
    if b == 0:
        print("Division par 0 impossible !")
        return
    
    q = 0
    r = a
    while r >= b:
        r -= b
        q += 1
    
    print("Quotient = ", q)
    print("Reste    = ", r)
    print("-----")

print("-----")
d1 = int(input("Dividende : "))
d2 = int(input("Diviseur : "))
print("-----")

de(d1, d2)
