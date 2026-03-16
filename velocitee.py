import time
from turtle import *
import kandinsky

ve = 1
pos = 0
veFact = 1.1

x=pos
y=100

def updateUI():
  x=int(round(pos,1))*2  
  kandinsky.fill_rect(0,0,1000,1000,'white')
  kandinsky.draw_string("VeFact : "+str(veFact) ,5,5)
  kandinsky.draw_string("Ve : "+str(ve) ,5,25)
  kandinsky.draw_string("pos : "+str(pos) ,5,45)
  kandinsky.fill_rect(x,y,10,10,'blue')

while True:
  veFact = float(input("VeFact : "))
  pos = 150
  ve = 1
  while pos != 0:
    ve = ve * veFact
    if (pos-ve) <= 0:
      pos = 0
    else:
      pos = pos - ve
    
    print("Pos :", pos, "Ve :", ve)
    updateUI()
    time.sleep(0.01)
    
