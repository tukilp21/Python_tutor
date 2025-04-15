import turtle
import math

# --- Setup screen ---
screen = turtle.Screen()
screen.title("🏎️ Turtle Drift GP")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off auto updates for smooth loop

# --- Draw track (simplified rectangle) ---
def draw_track():
    track = turtle.Turtle()
    track.speed(0)
    track.pensize(10)
    track.pencolor("gray")
    track.penup()
    track.goto(-300, -200)
    track.pendown()
    for _ in range(2):
        track.forward(600)
        track.left(90)
        track.forward(400)
        track.left(90)
    track.hideturtle()

draw_track()

# --- Create Car ---
car = turtle.Turtle()
car.shape("triangle")
car.color("red")
car.shapesize(1.5)
car.penup()
car.goto(-250, -180)
car.setheading(0)

# --- Movement Variables ---
velocity = 0
max_speed = 8
acceleration = 0.3
deceleration = 0.1
turn_speed = 3
friction = 0.05
inertia_x = 0
inertia_y = 0

# --- Control Flags ---
keys = {"w": False, "a": False, "s": False, "d": False}

def press_w(): keys["w"] = True
def release_w(): keys["w"] = False
def press_s(): keys["s"] = True
def release_s(): keys["s"] = False
def press_a(): keys["a"] = True
def release_a(): keys["a"] = False
def press_d(): keys["d"] = True
def release_d(): keys["d"] = False

# Bind keys
screen.listen()
screen.onkeypress(press_w, "w")
screen.onkeyrelease(release_w, "w")
screen.onkeypress(press_s, "s")
screen.onkeyrelease(release_s, "s")
screen.onkeypress(press_a, "a")
screen.onkeyrelease(release_a, "a")
screen.onkeypress(press_d, "d")
screen.onkeyrelease(release_d, "d")

# --- Game Loop ---
def game_loop():
    global velocity, inertia_x, inertia_y

    # Accelerate / Brake
    if keys["w"]:
        velocity += acceleration
    elif keys["s"]:
        velocity -= acceleration
    else:
        # Apply friction
        if velocity > 0:
            velocity -= deceleration
        elif velocity < 0:
            velocity += deceleration

    # Clamp velocity
    velocity = max(-max_speed / 2, min(max_speed, velocity))

    # Turn only if moving
    if abs(velocity) > 0.1:
        if keys["a"]:
            car.left(turn_speed)
        if keys["d"]:
            car.right(turn_speed)

    # Update inertia
    angle_rad = math.radians(car.heading())
    inertia_x = (1 - friction) * inertia_x + friction * velocity * math.cos(angle_rad)
    inertia_y = (1 - friction) * inertia_y + friction * velocity * math.sin(angle_rad)

    # Move car
    x = car.xcor() + inertia_x
    y = car.ycor() + inertia_y
    car.goto(x, y)

    # Update screen
    screen.update()
    screen.ontimer(game_loop, 20)

# --- Start ---
print("🏁 Turtle Drift GP")
print("W = Accelerate | S = Brake | A/D = Turn")
print("Try drifting around the track!")

game_loop()
screen.mainloop()
