from graph import *

x = 1500
y = 1000
windowSize(x,y)
canvasSize(x,y)
brushColor(0,200,200)
rectangle(0,0,x,y/2)
brushColor(0,128,0)
rectangle(0,y/2,x,y)
c=canvas()

line(910,660,850,900)
line(945,660,1005,900)#woman legs

c.create_oval(550,350,700,700,fill='black', outline = 'black')
brushColor(200,200,200)
circle(625,310,60)
brushColor(255,0,255)
triangle=[(925,310),(1030,700),(820,700)]
polygon(triangle)
brushColor(200,200,200)
circle(925,310,60)
line(680,410,780,550)#left hand men
line(567,410,450,550)#right hand man
line(898,410,780,550)#right hand women
line(952,410,1040,510)
line(1088,410,1040,510)#left hand woman
line(1100,320,1080,470)#ball stick
brushColor("red")
triangle2 = [(1100,320),(1150,250),(1060,240)]
penColor("red")
polygon(triangle2)
circle(1084,235,23)
circle(1128,239,23)#heart
brushColor("yellow")
penColor("yellow")
triangle3=[(450,550),(470,480),(420,480)]
polygon(triangle3)
brushColor("red")
penColor("red")
circle(462,480,17)
brushColor(255,255,255)
penColor(255,255,255)
circle(430,480,17)
brushColor(128,0,0)
penColor(128,0,0)
circle(438,465,17)#ice cream
penColor(0,0,0)
line(610,660,550,900)
line(650,660,700,900)#man legs


run()
