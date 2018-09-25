from turtle import *

def draw_circle():
  begin_fill()
  fillcolor('red')
  pencolor('green')
  width(10)
  circle(180)
  right(300)
  width(10)
  circle(180)
  end_fill()
  draw_circle()
  input()