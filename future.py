from math import *
import time
import graphics as gr

win = gr.GraphWin("f u t u r e",500,500,False)
win.setBackground("black")
msg = "welcome to the future"
ml = []
r = 0

def ez(w,h,o,v=0):
    global r
    x = w*cos(radians(r+o))+250
    y = h*sin(radians(r+o))+250+v
    return gr.Point(x,y)

for i in range(len(msg)):
    txt = gr.Text(gr.Point(550+(50*i),75),msg[i])
    txt.setFill("white")
    txt.setSize(25)
    txt.setStyle("bold")
    txt.draw(win)
    ml.append(txt)

cube = []
cube.append(gr.Line(ez(150,60,0,-30),ez(150,60,90,-30)))
cube.append(gr.Line(ez(150,60,90,-30),ez(150,60,180,-30)))
cube.append(gr.Line(ez(150,60,180,-30),ez(150,60,270,-30)))
cube.append(gr.Line(ez(150,60,270,-30),ez(150,60,0,-30)))

cube.append(gr.Line(ez(150,60,0,150),ez(150,60,90,150)))
cube.append(gr.Line(ez(150,60,90,150),ez(150,60,180,150)))
cube.append(gr.Line(ez(150,60,180,150),ez(150,60,270,150)))
cube.append(gr.Line(ez(150,60,270,150),ez(150,60,0,150)))

cube.append(gr.Line(ez(150,60,0,150),ez(150,60,0,-30)))
cube.append(gr.Line(ez(150,60,90,150),ez(150,60,90,-30)))
cube.append(gr.Line(ez(150,60,180,150),ez(150,60,180,-30)))
cube.append(gr.Line(ez(150,60,270,150),ez(150,60,270,-30)))

for i in cube:
    i.setWidth(4)
    i.setFill("white")
    i.draw(win)

hint = gr.Text(gr.Point(250,75),"c   l   i   c   k")
hint.setFill("white")
hint.setSize(25)
hint.setStyle("bold")
hint.draw(win)

win.getMouse()

hint.undraw()

while not win.closed:
    m = win.checkMouse()
    for i in cube:
        i.undraw()

    cube = []

    cube.append(gr.Line(ez(150,60,0,-30),ez(150,60,90,-30)))
    cube.append(gr.Line(ez(150,60,90,-30),ez(150,60,180,-30)))
    cube.append(gr.Line(ez(150,60,180,-30),ez(150,60,270,-30)))
    cube.append(gr.Line(ez(150,60,270,-30),ez(150,60,0,-30)))

    cube.append(gr.Line(ez(150,60,0,150),ez(150,60,90,150)))
    cube.append(gr.Line(ez(150,60,90,150),ez(150,60,180,150)))
    cube.append(gr.Line(ez(150,60,180,150),ez(150,60,270,150)))
    cube.append(gr.Line(ez(150,60,270,150),ez(150,60,0,150)))

    cube.append(gr.Line(ez(150,60,0,150),ez(150,60,0,-30)))
    cube.append(gr.Line(ez(150,60,90,150),ez(150,60,90,-30)))
    cube.append(gr.Line(ez(150,60,180,150),ez(150,60,180,-30)))
    cube.append(gr.Line(ez(150,60,270,150),ez(150,60,270,-30)))

    for i in cube:
        i.setWidth(4)
        i.setFill("white")
        i.draw(win)

    for i in range(len(msg)):
        ml[i].move(-2,75+(25*sin((r/10)+(i*5)))-ml[i].getAnchor().getY())

    if r == 810:
        for i in ml:
            i.move(1800,0)
        r = 0

    r += 1
    time.sleep(1/60)
    win.flush()