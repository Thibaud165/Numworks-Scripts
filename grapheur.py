import kandinsky
from turtle import *
from math import *
from ion import *

x=0
zoom=5
func = x
  
speed(10)

def axe():
  penup()
  pensize(1)
  goto(-160,0)
  pendown()
  color('black')
  goto(160,0)
  goto(0,0)
  goto(0,111)
  goto(0,-111)
  goto(0,0)
  penup()

def axek():
  kandinsky.fill_rect(0,110,320,1,'black')
  kandinsky.fill_rect(160,0,1,220,'black')
    
axek()

penup()
color('red')
pensize(2)
goto(-165,0)
pendown()
speed(10)
for y in range(-165,165):
  func = 2*x-6
  func = func
  x=y
  if round(func) <= 165:
    if round(func) >= -165:
      goto(y*zoom-zoom,round(func)*zoom)
    else:
      penup()
      goto(x,-165)
      pendown()
  else:
    penup()
    goto(x,165)
    pendown()
  kandinsky.draw_string(str(position()),0,0)
  kandinsky.draw_string(str(y),0,25)
