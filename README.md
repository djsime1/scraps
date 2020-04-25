# *DJ'(s crap)*
### Assorted python files with HD graphics!
Last update: 4/25/2020  
[Download zip of all files](https://github.com/djsime1/scraps/archive/master.zip)

## Table of Contents:
(In order of most epic to least epic)
- graphics.py
- spiral.py
- future.py
- ball.py
- joystick.py
- skittles.py

## graphics.py
The library that does all things!  
[(Using my forked version)](https://github.com/djsime1/pythonGraphics)

## Spirals! (spiral.py)
Points in a sphere. Scroll to modify turn factor.  
Try setting tf (turn factor) on line 7 to values like 0.5 or the golden ratio.  
If you're going to increase the count (number of dots) above 500, I recommend commenting out line 21 and changing line 22 to `c.setFill("white")`

## Spinning cube (future.py)
3D vector model proof of concept.

## Bouncing Ball (ball.py)
A very simple physics simulation.  
Click anywhere to teleport and speed up the ball.

## Joystick thing? (joystick.py)
Takes a point and returns a degree value upon a circle.  
Click anywhere to move along circle, or scroll to increase/decrease degree.

## Rainbow road (skittles.py)
Used to test my [middle click](https://github.com/djsime1/pythonGraphics/commit/3425d3586adb216c6d6421eb8d16e4785b498053) and [scroll detection](https://github.com/djsime1/pythonGraphics/commit/63820dc7ed55b9c1083d9447774c532257f2ad07) modifications to graphics.py.  
Scroll to scroll, middle click to print a message.