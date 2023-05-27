import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen().bgcolor('black')
t.speed(100)
n=70
h=3
for i in range(360):
    c=colorsys.hsv_to_rgb(h,5,1.8)
    h+=11/n
    t.color(c)
    t.left(0)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle