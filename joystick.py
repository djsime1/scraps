import graphics as gr
import math
import time

win = gr.GraphWin("joystick",500,500,False)
ring = gr.Circle(gr.Point(250,250),199)
deg = 0
win.setBackground("black")
ring.setFill("black")
ring.setWidth(2)
ring.setOutline("white")
ring.draw(win)

dot = gr.Circle(gr.Point(0,0),10)
dot.setWidth(0)
dot.setFill("blue")
dot.draw(win)

line = gr.Line(gr.Point(0,0),gr.Point(0,0))
line.setFill("green")
line.setWidth(2)
line.draw(win)

win.flush()

while not win.closed:
    mp = win.getCurrentMouseLocation()
    m = win.checkMouse()
    s = win.checkScroll()
    deg += s

    if m:
        deg = abs(math.degrees(math.atan2(m.x-250,m.y-250))-180)

    dot.undraw()
    dot = gr.Circle(gr.Point(200*math.cos(math.radians(deg-90))+250,200*math.sin(math.radians(deg-90))+250),20)
    dot.setWidth(0)
    dot.setFill("red")
    dot.draw(win)
    
    line.undraw()
    line = gr.Line(gr.Point(250,250),mp)
    line.setFill("green")
    line.setWidth(2)
    line.draw(win)

    win.flush()
    time.sleep(1/60)