from graph import *

x = 1400
y = 700
windowSize(x,y)
canvasSize(x,y)
brushColor(0,200,200)
rectangle(0,0,x,y/2)
brushColor(0,128,0)
rectangle(0,y/2,x,y)
c=canvas()

c.create_oval(210,320,310,520,fill='#808080', outline = '#808080')
c.create_oval(1100,320,1200,520,fill='#808080', outline = '#808080')

line(520,520,500,620)
line(580,520,600,620)#legs left woman

line(820,520,800,620)
line(880,520,900,620)#legs right woman

line(250,520,240,620)
line(270,520,280,620)#legs left man

line(1140,520,1120,620)
line(1160,520,1180,620)#legs right man

line(1100,620,1120,620)
line(1200,620,1180,620)#right man little legs

line(220,620,240,620)
line(300,620,280,620)#left man little legs

line(500,620,480,620)
line(600,620,620,620)#left girl little legs

line(920,620,900,620)
line(780,620,800,620)#right girl little legs

triangleA=[(550,320),(500,520),(600,520)]
triangleB=[(850,320),(800,520),(900,520)]
brushColor(255,0,255)
polygon(triangleA)
polygon(triangleB)
brushColor(200,200,200)
circle(260,290,40)
circle(550,290,40)
circle(850,290,40)
circle(1150,290,40)
line(410,420,290,340)#left hand left man
line(410,420,545,340)#right hand left woman
line(1300,420,1180,340)#left hand right man
line(990,420,855,340)#left hand right woman
line(110,420,230,340)#right hand left man
line(990,420,1120,340)#right hand right man
line(775,380,845,340)
line(695,340,775,380)#right hand right woman
line(615,380,555,340)
line(695,340,615,380)#left hand woman

brushColor("yellow")
penColor("yellow")
triangle3=[(650,250),(670,180),(620,180)]
polygon(triangle3)
brushColor("red")
penColor("red")
circle(662,180,17)
brushColor(255,255,255)
penColor(255,255,255)
circle(630,180,17)
brushColor(128,0,0)
penColor(128,0,0)
circle(638,165,17)#ice cream

line(650,250,695,340)#ice cream stick

brushColor("yellow")
penColor("yellow")
triangle3=[(1300,415),(1335,330),(1285,330)]
polygon(triangle3)
brushColor("blue")
penColor("blue")
circle(1327,330,17)
brushColor(255,255,255)
penColor(255,255,255)
circle(1295,330,17)
brushColor(128,0,0)
penColor(128,0,0)
circle(1303,315,17)#ice cream man

brushColor("red")
triangle2 = [(100,320),(150,250),(60,240)]
penColor("red")
polygon(triangle2)
circle(84,235,23)
circle(128,239,23)#heart

line(100,320,110,420)



run()
