print("Obtenir :")
print("1. |x-...|<= ... avec [A,B]")
print("2. [...,...] avec centre et rayon ")

print()
choix=int(input("Choix : "))
print()

if choix == 1:
  while True:
    a=float(input("A : "))
    b=float(input("B : "))
    c = (a+b)/2
    r = b-c
    print()
    print("centre =", c)
    print("rayon =", r)
    print()
    
elif choix == 2:
  while True:
    c=float(input("centre : "))
    r=float(input("rayon : "))
    signe = c[0]
    a = c-r
    b = c+r
    print()
    print("[",a,";",b,"]")
    print()
