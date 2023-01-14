import turtle as t
import colorsys

t.bgcolor('black')
t.setpos(-90,80)
t.tracer(100)
t.pensize(2)
hue = 0.0
t.hideturtle()

for i in range(600):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    t.fd(200)
    t.rt(91)
    t.circle(50)
    hue +=0.009
done()

