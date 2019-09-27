from graph import *
import random
l = 1500
h = 1000
windowSize(l,h)
canvasSize(l,h)
brushColor(0,200,200)
rectangle(0,0,l,h/2)
brushColor(0,128,0)
rectangle(0,h/2,l,h)
c=canvas()


def oval(x1, y1, x2, y2, r):
    j = ((x1 + x2) / 2) - r
    k = ((y1 + y2) / 2) - r
    for j in range(((int(x1 + x2)) // 2) + int(r)):
        for k in range((int(y1 + y2) // 2) + int(r)):
            if ((j - x1) ** 2 + (k - y1) ** 2) ** (0.5) + ((j - x2) ** 2 + (k - y2) ** 2) ** (0.5) <= r:
                point(int(j), int(k))

def face(x, y, byka):
    m=1
    k=1


    penColor('black')
    oval(k * (x + m * 20), k * (y - 40), k * (x + m * 35), k * (y - 40), k * 18)
    penColor('white')
    oval(k * (x + m * 20), k * (y - 40), k * (x + m * 35), k * (y - 40), k * 16)
    penColor('black')
    brushColor('black')
    circle(k * (x + m * 28), k * (y - 40), k * 3)

    penColor('black')
    oval(k * (x - m * 15), k * (y - 40), k * (x), k * (y - 40), k * 18)
    penColor('white')
    oval(k * (x - m * 15), k * (y - 40), k * (x), k * (y - 40), k * 16)
    penColor('black')
    brushColor('black')
    circle(k * (x - m * 8), k * (y - 40), k * 3)
    penColor('black')
    oval(k * (x - 15 * m), k * (y - 5), k * (x + m * 35), k * (y - 5), k * 55)
    penColor(200,200,200)
    if byka>0.5:
        oval(k * (x - m * 15), k * (y - 13), k * (x + m * 35), k * (y - 13), k * 55)
    else:
        oval(k * (x - m * 15), k * (y - 3), k * (x + m * 35), k * (y - 3), k * 55)

def couple(x,y):
    line(910+x,660+y,850+x,900+y)
    line(945+x,660+y,1005+x,900+y)#woman legs

    c.create_oval(550+x,350+y,700+x,700+y,fill='black', outline = 'black')
    brushColor(200,200,200)
    circle(625+x,310+y,60)
    face(620+x, 315+y, random.random())
    brushColor(255,0,255)
    triangle=[(925+x,310+y),(1030+x,700+y),(820+x,700+y)]
    polygon(triangle)
    brushColor(200,200,200)
    circle(925+x,310+y,60)
    face(920+x, 315+y, random.random())
    line(680+x,410+y,780+x,550+y)#left hand men
    line(567+x,410+y,450+x,550+y)#right hand man
    line(898+x,410+y,780+x,550+y)#right hand women
    line(952+x,410+y,1040+x,510+y)
    line(1088+x,410+y,1040+x,510+y)#left hand woman
    line(1100+x,320+y,1080+x,470+y)#ball stick
    brushColor("red")
    triangle2 = [(1100+x,320+y),(1150+x,250+y),(1060+x,240+y)]
    penColor("red")
    polygon(triangle2)
    circle(1084+x,235+y,23)
    circle(1128+x,239+y,23)#heart
    brushColor("yellow")
    penColor("yellow")
    triangle3=[(450+x,550+y),(470+x,480+y),(420+x,480+y)]
    polygon(triangle3)
    brushColor("red")
    penColor("red")
    circle(462+x,480+y,17)
    brushColor(255,255,255)
    penColor(255,255,255)
    circle(430+x,480+y,17)
    brushColor(128,0,0)
    penColor(128,0,0)
    circle(438+x,465+y,17)#ice cream
    penColor(0,0,0)
    line(610+x,660+y,550+x,900+y)
    line(650+x,660+y,700+x,900+y)#man legs



#couple(100, 200)

for i in range(4):
     for k in range(5):
         couple(i*l/3-200, k*h/5)

run()