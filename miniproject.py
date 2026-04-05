import turtle
import math
import time

# ---------------- SCREEN ----------------
wn = turtle.Screen()
wn.setup(width=800, height=600)
wn.title("Archery Game")
wn.bgcolor("white")
wn.tracer(0)

# ---------------- PENS ----------------
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

ui = turtle.Turtle()
ui.hideturtle()
ui.penup()

target = turtle.Turtle()
target.hideturtle()
target.penup()

# ---------------- ARROW ----------------
arrow = turtle.Turtle()
arrow.shape("triangle")
arrow.color("brown")
arrow.penup()
arrow.goto(-300, 0)

# ---------------- STATE ----------------
screen_state = "intro"
angle = 0
shooting = False
speed = 15
score = 0
attempts = 5

# ---------------- INTRO ----------------
def show_intro():
    pen.clear()
    ui.clear()
    target.clear()

    wn.bgcolor("#e6f2ff")

    pen.goto(0, 100)
    pen.write("ARCHERY GAME", align="center", font=("Arial", 30, "bold"))

    pen.goto(0, 0)
    pen.write("Press ENTER to Continue", align="center", font=("Arial", 16))

# ---------------- INSTRUCTIONS ----------------
def show_instructions():
    pen.clear()
    ui.clear()
    target.clear()

    wn.bgcolor("#fff5e6")

    pen.goto(0, 150)
    pen.write("HOW TO PLAY", align="center", font=("Arial", 26, "bold"))

    pen.goto(0, 20)
    pen.write(
        "UP   : Increase Angle\n"
        "DOWN : Decrease Angle\n"
        "SPACE: Shoot Arrow\n\n"
        "Press ENTER to Start",
        align="center",
        font=("Arial", 16)
    )

# ---------------- TARGET ----------------
def draw_target():
    target.clear()
    colors = ["red", "white", "red", "white", "red"]
    radius = 60

    for color in colors:
        target.goto(250, -radius)
        target.color(color)
        target.begin_fill()
        target.circle(radius)
        target.end_fill()
        radius -= 12

# ---------------- GAME ----------------
def start_game():
    pen.clear()
    ui.clear()
    target.clear()

    wn.bgcolor("skyblue")

    arrow.goto(-300, 0)
    arrow.setheading(0)

    draw_target()

# ---------------- SCREEN SWITCH ----------------
def next_screen():
    global screen_state

    if screen_state == "intro":
        screen_state = "instructions"
        show_instructions()

    elif screen_state == "instructions":
        screen_state = "game"
        start_game()

# ---------------- CONTROLS ----------------
def angle_up():
    global angle
    if screen_state == "game" and not shooting:
        angle += 5
        arrow.setheading(angle)

def angle_down():
    global angle
    if screen_state == "game" and not shooting:
        angle -= 5
        arrow.setheading(angle)

def shoot():
    global shooting
    if screen_state == "game" and not shooting:
        shooting = True

# ---------------- KEY BINDINGS ----------------
wn.listen()
wn.onkeypress(next_screen, "Return")
wn.onkeypress(angle_up, "Up")
wn.onkeypress(angle_down, "Down")
wn.onkeypress(shoot, "space")

# ---------------- START ----------------
show_intro()

# ---------------- LOOP ----------------
while True:
    wn.update()

    if screen_state == "game":

        if shooting:
            x = arrow.xcor() + speed * math.cos(math.radians(angle))
            y = arrow.ycor() + speed * math.sin(math.radians(angle))
            arrow.goto(x, y)

            dist = arrow.distance(250, 0)

            if dist < 60:
                shooting = False
                score += 10
                arrow.goto(-300, 0)
                arrow.setheading(angle)

            if x > 400 or y > 300 or y < -300:
                shooting = False
                arrow.goto(-300, 0)
                arrow.setheading(angle)

        # UI
        ui.clear()
        ui.goto(-350, 250)
        ui.write(f"Score: {score}   Angle: {angle}",
                 font=("Arial", 14, "bold"))

    time.sleep(0.02)


