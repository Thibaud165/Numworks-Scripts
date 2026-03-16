from kandinsky import *
from ion import *
from time import *

x = 50

fill_rect(0,0,1000,1000,'black')
fill_rect(10,10,90,145,'gray')
fill_rect(20,20,70,125,'white')

def gui():  
  fill_rect(20,20,70,125,'white')
  fill_rect(20,20,70,round(125-(x/2)),'orange')
  fill_rect(170,30,100,40,'orange')
  draw_string("h = "+str(x),180,40)
  fill_rect(170,70,100,40,'white')
  draw_string("x = "+str(250-x),180,80)
  draw_string("Appuyer sur + ou - ",0,202)

gui()
while True:  
  if keydown(KEY_PLUS):
    if x < 250:
      x += 1
      gui()
    
  if keydown(KEY_MINUS):
    if x > 0: 
      x -= 1
      gui()
