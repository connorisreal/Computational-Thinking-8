import time, turtle, random
from utils import *
# Section 1: Setup
# set_background("castle")
s1 = create_sprite("cardinal2",0,-200)
drawing = False
hidden = False

# Section 2: define controls
def move_up1():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y+4)
        
def move_down1():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y-4)
    
def move_left1():
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x-4, y)
    
def move_right1(): 
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x+4, y)

def toggle_drawing():
    global drawing
    if drawing == False:
        s1.pendown()
        drawing = True
    else:
        s1.penup()
        drawing = False

def erase():
    s1.clear()

window.onkeypress(move_up1, "Up")
window.onkeypress(move_down1, "Down")
window.onkeypress(move_left1, "Left")
window.onkeypress(move_right1, "Right")
window.onkeypress(toggle_drawing, "c")
window.onkeypress(erase, "space")

# Section 3: define other controls
def toggle_hiding():
    global hidden
    if hidden == False:
        s1.showturtle()
        hidden = True
    else:
        s1.hideturtle()
        hidden = False

window.onkeypress(toggle_hiding, "h")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()