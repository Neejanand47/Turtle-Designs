import turtle as t


t.speed(0)
t.bgcolor("black")
colors=["blue","cyan","cyan"]
t.pensize(2)
a=200
for i in range(160):
                t.color(colors[i%3])
                t.circle(a,90)
                t.lt(90)
                t.circle(a,90)
                t.lt(18)
                a-=1