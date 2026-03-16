from ion import *
from kandinsky import *
import random
import time

exe = int(input("EXE ? (0/1) : "))
graph = int(input("Graph (2-10) : "))

if exe == 0:
  speed = 0.5
else:
  speed = 1

if graph > 1 and graph < 11: 
  nbr_graph = graph
else:
  while True:
    print("graph input error")

last = 0
bleu = 0
rouge = 0
vert = 0
jaune = 0
marron = 0
white = 0
pink = 0
orange = 0
violet = 0
gris = 0

i = 0

fill_rect(0,0,1000,1000,'black')

def draw():
  global i
  draw_string("Iteration "+str(i),0,0)
  fill_rect(0,30,t_bleu,10,'blue')
  fill_rect(0,50,t_rouge,10,'red')
  if graph >= 3:
    fill_rect(0,70,t_vert,10,'green')
  if graph >= 4:
    fill_rect(0,90,t_jaune,10,'yellow')
  if graph >= 5:
    fill_rect(0,110,t_marron,10,'brown')
  if graph >= 6:
    fill_rect(0,130,t_white,10,'white')
  if graph >= 7:
    fill_rect(0,150,t_pink,10,'pink')
  if graph >= 8:
    fill_rect(0,170,t_orange,10,'orange')
  if graph >= 9:
    fill_rect(0,190,t_violet,10,'purple')
  if graph >= 10:
    fill_rect(0,210,t_gris,10,'gray')


while True:
  if exe == 1:
    pressed = 2
    while pressed != 0:
      if keydown(KEY_EXE):
        pressed = 0

  i = i + 1
  last = random.randint(0,graph-1)
  if last == 0: bleu = bleu + speed
  if last == 1: rouge = rouge + speed
  if last == 2: vert = vert + speed
  if last == 3: jaune = jaune + speed
  if last == 4: marron = marron + speed
  if last == 5: white = white + speed
  if last == 6: pink = pink + speed
  if last == 7: orange = orange + speed
  if last == 8: violet = violet + speed
  if last == 9: gris = gris + speed
  t_bleu = int(round(bleu,0))
  t_rouge = int(round(rouge,0))
  t_vert = int(round(vert,0))
  t_jaune = int(round(jaune,0))
  t_marron = int(round(marron,0))
  t_white = int(round(white,0))
  t_pink = int(round(pink,0))
  t_orange = int(round(orange,0))
  t_violet = int(round(violet,0))
  t_gris = int(round(gris,0))
  draw()
