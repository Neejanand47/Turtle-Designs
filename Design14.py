import turtle as tr
import colorsys

tr.Screen().bgcolor('blue')
t = tr.Turtle()
t.speed(0)
h = 0
t.pensize(3)

def design(n):
    t.forward(n)
    t.circle(-50,45)
    t.forward(n)
    t.circle(50,180)

t.setpos(-20,0)
t.seth(22)

for i in range(200):
    c = colorsys.hsv_to_rgb(h, 0.8, 1)
    t.pencolor(c)
    design(i*0.5)
    design(i)
    h += 0.005
t.ht()
done()
