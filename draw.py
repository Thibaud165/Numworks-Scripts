from ion import *
import turtle as t
from kandinsky import *
from time import *

t.penup()
t.goto(0,0)
t.setheading(90)
t.pendown()

colors = ['blue', 'red', 'green', 'yellow', 'brown', 'black', 'white', 'pink', 'orange', 'purple', 'gray']
color_index = 6
brush_size = 2
step = 1
speed = 10

def draw_gui():
  # bg  
  fill_rect(0, 0, 320, 40, color(150,150,150))
  # color
  fill_rect(10, 10, 20, 20, colors[color_index - 1])
  t.color(colors[color_index - 1])
  # size
  draw_string("Size : "+str(brush_size),40,10)
  # speed
  draw_string("Speed : "+str(speed),150,10)

draw_gui()
t.pensize(brush_size)
t.speed(speed)
while True:  
  if keydown(KEY_EIGHT):
    t.setheading(90)
    t.forward(step)
    draw_gui()
  if keydown(KEY_SIX):
    t.setheading(0)
    t.forward(step)
    draw_gui()
  if keydown(KEY_TWO):
    t.setheading(270)
    t.forward(step)
    draw_gui()
  if keydown(KEY_FOUR):
    t.setheading(180)
    t.forward(step)
    draw_gui()
  if keydown(KEY_SEVEN):
    t.setheading(135)
    t.forward(step)
    draw_gui()
  if keydown(KEY_NINE):
    t.setheading(45)
    t.forward(step)
    draw_gui()
  if keydown(KEY_THREE):
    t.setheading(315)
    t.forward(step)
    draw_gui()
  if keydown(KEY_ONE):
    t.setheading(225)
    t.forward(step)
    draw_gui()

  if keydown(KEY_PLUS):
    brush_size += 1
    t.pensize(brush_size)
    draw_gui()
    while keydown(KEY_PLUS):
      sleep(0)
  if keydown(KEY_MINUS):
    if brush_size > 0:
      brush_size -= 1
      t.pensize(brush_size)
      draw_gui()
      while keydown(KEY_MINUS):
        sleep(0)
  
  if keydown(KEY_MULTIPLICATION):
    if color_index < 10:  
      color_index += 1
      t.color(colors[color_index])
      draw_gui()
    while keydown(KEY_MULTIPLICATION):
      sleep(0)
  if keydown(KEY_DIVISION):
    if color_index > 0:  
      color_index -= 1
      t.color(colors[color_index])
      draw_gui()
    while keydown(KEY_DIVISION):
      sleep(0)
    
  if keydown(KEY_LEFTPARENTHESIS):
    speed = max(1, speed - 1)
    t.speed(speed)
    draw_gui()
    while keydown(KEY_LEFTPARENTHESIS):
      sleep(0)
  if keydown(KEY_RIGHTPARENTHESIS):
    speed = min(10, speed + 1)
    t.speed(speed)
    draw_gui()
    while keydown(KEY_RIGHTPARENTHESIS):
      sleep(0)
    
  if keydown(KEY_EXE):
    t.penup()
    t.reset()
    t.showturtle()
    t.speed(10)
    t.pensize(0)
    t.goto(100,0)
    t.reset()
    t.setheading(90)
    t.pendown()
    t.pensize(brush_size)
    t.speed(speed)
    draw_gui()
    while keydown(KEY_EXE):
      sleep(0)
