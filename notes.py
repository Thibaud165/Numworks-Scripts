from kandinsky import *

resultat_final = 0
dividende_final = 0
pas = 5
desir = 5

def note(resul, divid, desir):
  global resultat_final, dividende_final
  resultat_final = (resul*desir)/divid
  dividende_final = divid

while True:  
  # input
  print()
  print("Note :")
  in_note = input()
  print()
  print("Dividende :")
  in_divid = input()
  
  # bg
  fill_rect(0,0,175,300,'gray')
  fill_rect(175,0,200,300,'blue')
  
  # note de base
  disp_full_entry = str(in_note + "/" + in_divid)
  draw_string(str(disp_full_entry),50,100)
  
  # desir
  for i in range(0,10):
    desir_r = desir(float(in_note), float(in_divid), 20)
    print(desir_r)
    #draw_string(str(desir_r),200,100)
  
