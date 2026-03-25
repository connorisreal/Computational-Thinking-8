# Section 1 - Your code
from utils import *
import time as t
player_name = input("What is your name?    ")

set_background("hell")

s1 = create_sprite("turtle2", -200, 0)
s2 = create_sprite("turtle3", 200, 0)

s1.color("blue")
s2.color("white")
t.sleep(5)

s1.write("Where are we?",font = ("Arial", 10, "normal"))
window.update()
t.sleep(1)

s1.clear()
window.update()
t.sleep(1)

s2.write("Not on the moon!",font = ("Arial", 10, "normal"))
window.update()
t.sleep(1)

s2.clear()
window.update()
t.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 10, "normal"))
window.update()
t.sleep(1)

s1.clear()
s1.write("Have you seen them?",font = ("Arial", 10, "normal"))
window.update()
t.sleep(1)

s2.clear()
s2.write("No, why?", font=("Arial",10,"normal"))
window.update()
s1.clear()
t.sleep(1)

for i in range(20):
    t.sleep(0.03)
    s1.setheading(120)
    s1.forward(5)
    window.update()


s2.clear()
s2.hideturtle()
set_background("nyc")

s1.setpos(200,50)
window.update()

s3 = create_sprite("bald_eagle",-250,0)
s3.color("white")
s3.write("Hi",font=("arial",10,"normal"))
window.update()
t.sleep(1)
s3.clear()

s1.write("I'm looking for " + player_name + " have you seen them?",font=("arial",10,"normal"))
window.update()
t.sleep(1)
s1.clear()

s3.write("Yeah, he's vacationing in Hawaii",("arial",10,"normal"))
window.update()
t.sleep(1)
s3.clear()

s1.write("OK",("arial",10,"normal"))
######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()