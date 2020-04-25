import graphics as gr
from math import *
from colorsys import hsv_to_rgb
import time

count = 500
tf = 0 #(1+sqrt(5))/2 #Golden ratio
dots = []
win = gr.GraphWin("Spiral",600,600,False)
win.setBackground("black")

def draw():
    global count
    global dots
    for i in range(count):
        dist = sqrt(i/count)*250
        ang = 2*pi*tf*i
        x = dist*cos(ang)
        y = dist*sin(ang)
        c = gr.Circle(gr.Point(x+300,y+300),2)
        v = hsv_to_rgb(i/count,1,1)
        c.setFill(gr.color_rgb(int(v[0]*255),int(v[1]*255),int(v[2]*255)))
        c.setWidth(0)
        c.draw(win)
        dots.append(c)

draw()
win.flush()

while not win.closed:
    m = win.checkScroll()
    if m:
        for i in dots:
            i.undraw()
        dots = []
        tf += 0.00001*m
        draw()
        win.flush()
    #time.sleep(1/30)