import turtle

import colorsys

turtle.bgcolor("black")

squary = turtle.Turtle()
squary.speed(20)
h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        squary.color(c)
        h += 0.005
        squary.rt(90)
        squary.circle(150 - j * 6, 90)
        squary.lt(90)
        squary.circle(150 - j * 6, 90)
        squary.rt(180)
    squary.circle(40, 24)
squary.done()        


