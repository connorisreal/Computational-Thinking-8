from utils import *
cookies = 0
cursors = 0
cursor_cost = 20
grandmas = 0
grandma_cost = 100
tick = 0

set_background("black")

cookie = create_sprite("cookie_2", -225,0)
m1 = create_sprite("alien", -300, 130)
m1.color("white")
m1.hideturtle()

def cookie_click():
    global cookies
    cookies += 1

def show_variables():
    m1.write(f"Cookies: {cookies}\nCursors: {cursors}\nGrandmas: {grandmas}", font=("Arial", 24, "bold"))

def get_grandma():
    global grandmas, cookies, grandma_cost
    if cookies >= grandma_cost:
        cookies -= grandma_cost
        grandmas += 1
        grandma_cost = int(grandma_cost * 1.5)

def get_cursor():
    global cursors, cookies, cursor_cost
    if cookies >= cursor_cost:
        cookies -= cursor_cost
        cursors += 1
        cursor_cost = int(cursor_cost * 1.5)

window.onkeypress(cookie_click, "space") # adds one cookie to the cookies variable
window.onkeypress(get_grandma, "g") # buys one grandma
window.onkeypress(get_cursor, "c") # buys one cursor

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    tick += 1
    if tick >= 10:
        cookies += cursors
        cookies += grandmas * 5
        tick = 0

    m1.clear()
    show_variables()

    time.sleep(0.1)
    window.update()

# the goal is simply to get as many cookies as possible, and you can buy grandmas and cursors to passively get cookies!