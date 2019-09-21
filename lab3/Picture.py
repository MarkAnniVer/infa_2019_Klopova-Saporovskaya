from graph import *

x = 1000
y = 1000
windowSize(x,y)
canvasSize(x,y)
penColor("black")
brushColor("yellow")
circle(500,500,200)
brushColor("red")
circle(400,450,40)
circle(600,450,35)
brushColor("black")
circle(400,450,20)
circle(600,450,20)
brushColor("black")
rectangle(400,550,600,600)
a=[(450,450),(370,400),(350,380),(370,370)]
polygon(a)
b=[(490,410),(650,410),(550,350)]
polygon(b)
run()
