import turtle as t
from turtle import Screen



def koch(t, order, size):
    if order == 0:
    	t.setup(width=1000, height=1000)
    	t.penup()
    	t.pendown()
        t.forward(size)
        ts = t.getscreen()
        ts.getcanvas().postscript(file="duck.eps")
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)


koch(t,3,200)