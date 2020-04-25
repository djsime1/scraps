from graphics import *
from colorsys import hsv_to_rgb

win = GraphWin("taste the rainbow",400,300,False)
pos = 0

bars = []
for i in range(360*3):
    bars.append(Rectangle(Point(0,i*4),Point(400,i*4+4)))
    bars[i].setWidth(0)
    r = int(hsv_to_rgb(i/360,1,1)[0]*255)
    g = int(hsv_to_rgb(i/360,1,1)[1]*255)
    b = int(hsv_to_rgb(i/360,1,1)[2]*255)
    bars[i].setFill(color_rgb(r,g,b))
    bars[i].move(0,-360*4)
    bars[i].draw(win)

win.flush()

while not win.closed:
    time.sleep(1/60)
    m = win.checkMouseMiddle()
    s = win.checkScroll()
    if m:
        print("this demo is sponsored by skittles")

    if s != 0:
        for i in bars:
            i.move(0,s*16)
    