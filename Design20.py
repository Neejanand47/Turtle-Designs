# import turtle
from turtle import *

wn = Screen()
wn.setup(width = 1200, height = 680)
t = Turtle()
wn.bgcolor('black')
t.speed(10)
r,g,b = 255,0,0

for i in range(255*2):
    colormode(255)
    if i<255//3 :
        g+=3
    elif i<255*2//3 :
        r-=3
    elif i<255 :
        b+=3
    elif i<255*4//3 :
        g-=3
    elif i<255*5//3 :
        r+=3
    else :
        b-=3
    right(91)
    fd(i+1)
    pencolor(r,g,b)
wn.mainloop()