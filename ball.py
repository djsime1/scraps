# <[ IMPORTS ]>

import graphics as gr
import time

# <[ VARIABLES ]>

w = 1400
h = 700
xpos = 150
ypos = 150
xvel = 50
yvel = -50
rad = 50
win = gr.GraphWin("Ball demo",w,h)

# <[ FUNCTIONS ]>

def bounce(x,y):
    global xvel
    global yvel
    print("Boing!")
    if x:
        xvel = xvel*-.8
    if y:
        yvel = yvel*-.8

def moveto(o,x,y=None):
    if y != None: # X and Y given
        ox = o.getCenter().x
        oy = o.getCenter().y
        dx = x - ox
        dy = y - oy
        o.move(dx,dy)
    else: # Point given
        y = x.y
        x = x.x
        ox = o.getCenter().x
        oy = o.getCenter().y
        dx = x - ox
        dy = y - oy
        o.move(dx,dy)

# <[ MAIN ]>

win.setBackground("dimgray")
c = gr.Circle(gr.Point(xpos,ypos),rad)
c.setFill("seagreen4")
c.setWidth(2)
c.setOutline("seagreen1")
c.draw(win)

p = win.getMouse()
#moveto(c,p)

while True:
    time.sleep(.015)
    p = win.checkMouse()
    if p:
        moveto(c,p)
        xvel*=1.2
        yvel*=1.2

    xpos = c.getCenter().x
    ypos = c.getCenter().y
    yvel+=2
    if ypos+(yvel/10)>=h-rad or ypos+(yvel/10)<=rad:
        bounce(0,1)
    if xpos+(xvel/10)>=w-rad or xpos+(xvel/10)<=rad:
        bounce(1,0)
    if ypos <= rad:
        yvel+=2
    c.move(xvel/10,yvel/10)

win.close()