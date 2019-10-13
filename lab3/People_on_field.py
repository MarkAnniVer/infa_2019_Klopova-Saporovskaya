from graph import *
c = canvas()

x = 1400
y = 700
m = x / 15
t = 2 * y / 7
R = 40
# (x, y) is a size of the picture.
# R is head radius.
# m, t are parametres for drowing.
windowSize(x, y)
canvasSize(x, y)

def sky():
    brushColor(0, 200, 200)
    rectangle(0, 0, x, y / 2)
    # Draw blue sky.
	
def ground():
    brushColor(0, 128, 0)
    rectangle(0, y / 2, x, y)
    # Draw ground.
	
def man(x_left):
    penColor("black")
    line(x_left + m*(1 + 2/5), 5/2*t - 20,
         x_left + m*(1 + 1/5), 7/2*t - 20)
    line(x_left + m*(1 + 3/5), 5/2*t - 20,
         x_left + m*(1 + 4/5), 7/2*t - 20)
    line(x_left, 2 * t,
         x_left + m*1.5, (3/2 + 1/12)*t)
    line(x_left + 3*m, 2 * t,
         x_left + m*1.5, (3/2 + 1/12)*t)
    c.create_oval(x_left + m, 1.5 * t,
                  x_left + 2*m, 2.5 * t,
    			  fill = '#808080', 
    			  outline = '#808080')
    brushColor(200, 200, 200)
    penColor(200, 200, 200)
    circle(x_left + 3*m/2,
           1.5*t - R/2.5,
    	   R)
    # Draw man with indent x_left 
	# from left border.
	   
def woman(x_left):
    penColor("black")
    line(x_left + m*(1 + 2/5), 5/2*t - 20,
         x_left + m*(1 + 1/5), 7/2*t - 20)
    line(x_left + m*(1 + 3/5), 5/2*t - 20,
         x_left + m*(1 + 4/5), 7/2*t - 20)
    brushColor(255, 0, 255)
    penColor(255, 0, 255)
    triangleA = [
        (x_left + 1.5*m, 3/2*t),
    	(x_left + m, 5/2*t),
    	(x_left + 2*m, 5/2*t)
    	]
    polygon(triangleA)
    brushColor(200, 200, 200)
    penColor(200, 200, 200)
    circle(x_left + 3*m/2,
           1.5*t - R/4,
    	   R)
    # Draw woman with indent x_left 
	# from left border.
    	   
def heart(x_bottom, y_bottom):
    brushColor("red")
    penColor("red")
    triangle2 = [
        (x_bottom, y_bottom),
    	(x_bottom + 50, y_bottom - 70),
    	(x_bottom - 40, y_bottom - 80)
    	]
    polygon(triangle2)
    circle(x_bottom - 16,
           y_bottom - 85,
    	   23)
    circle(x_bottom + 28, 
           y_bottom - 81,
    	   23)
    # Draw heart with indent x_bottom from left border 
    # and y_bottom from upper border.
		   
def ice_cream(x_bottom, y_bottom):
    brushColor("yellow")
    penColor("yellow")
    triangle3 = [
        (x_bottom, y_bottom),
        (x_bottom + 20, y_bottom - 70),
        (x_bottom - 30, y_bottom - 70)
        ]
    polygon(triangle3)
    brushColor("red")
    penColor("red")
    circle(x_bottom + 12,
           y_bottom - 70,
    	   17)
    brushColor(255, 255, 255)
    penColor(255, 255, 255)
    circle(x_bottom - 20,
           y_bottom - 70,
    	   17)
    brushColor(128, 0, 0)
    penColor(128, 0, 0)
    circle(x_bottom - 12,
           y_bottom - 85,
    	   17)
    # Draw ice ceam with indent x_bottom from left border 
    # and y_bottom from upper border.
	
def woman_hands():
    line(x/10 + 3*m, 2 * t, 
	     x*3/10 + 1.5*m, 3/2*t + R)
    line(x*3/10 + 1.5*m, 3/2*t + R, 
         x*3/10 + 3*m, 7/4*t + R)
    line(x * 7 / 10, 2 * t, 
	     x*7/10 - 1.5*m, 3/2*t + R)
    line(x*7/10 - 1.5*m, 3/2*t + R, 
         x*3/10 + 3*m, 7/4*t + R)
    # Draw woman's hands

def stick(x1, y1, x2, y2):
    penColor("black")
    line(x1, y1, x2, y2)
	# Draw stick: (x1, y1) is a beginning 
	# (x2, y2) is the end
    
sky()
ground()
woman_hands()
man(x / 10)
man(x * 7 / 10)
woman(x * 3 / 10)
woman(x * 5 / 10)
stick(x / 10, 2 * t, 
      x / 11, 3 / 2 * t)
stick(x*3/10 + 3*m, 7/4*t + R, 
      x*3/10 + 2.5*m, t + R)
heart(x / 11, 3 / 2 * t)
ice_cream(x*3/10 + 2.5*m, t + R)
ice_cream(x*7/10 + 3*m, 2 * t)
run()
