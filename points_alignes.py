debug = True

if debug : print("Debug mod : on")
if debug : print()

print("Entrer points de repere sur :")
print()
rep1x = float(input("Repere 1 x : "))
rep1y = float(input("Repere 1 y : "))
print()
rep2x = float(input("Repere 2 x : "))
rep2y = float(input("Repere 2 y : "))
print()

parcour_rep_x = abs((rep1x)-(rep2x))
if debug : print("Parcours x :", parcour_rep_x)
parcour_rep_y = abs((rep1y)-(rep2y))
if debug : print("Parcours y :", parcour_rep_y)
coef_reel = abs(parcour_rep_x/parcour_rep_y)
if debug : print("Coef de deplacement :", coef_reel)
if debug : print()

while True:
  verifx = float(input("x du point a verif : "))
  verify = float(input("y du point a verif : "))
  print()
  
  parcour_ver_x = abs((rep1x)-(verifx))
  if debug : print("Parcours x :", parcour_ver_x)
  parcour_ver_y = abs((rep1y)-(verify))
  if debug : print("Parcours y :", parcour_ver_y)
  coef_comp = abs(parcour_ver_x/parcour_ver_y)
  if debug : print("Coef comparer :", coef_comp)
  if debug : print()
  
  if abs(coef_reel) == abs(coef_comp):
    print("="*28)
    print("Oui, les points sont alignes")
    print("="*28)
  else:
    print("="*35)
    print("Non, les points ne sont pas alignes")
    print("="*35)
  print()
