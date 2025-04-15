import turtle
import random
import time

# --- Setup Screen ---
screen = turtle.Screen()
screen.title("Turtle Coordinate Explorer")
screen.setup(width=700, height=700)
screen.setworldcoordinates(-5, -5, 5, 5)
screen.bgcolor("white")

# --- Draw Grid and Axes ---
grid_drawer = turtle.Turtle()
grid_drawer.hideturtle()
grid_drawer.speed(0)
grid_drawer.pencolor("lightgray")

for i in range(-5, 6):
    grid_drawer.penup()
    grid_drawer.goto(-5, i)
    grid_drawer.pendown()
    grid_drawer.goto(5, i)
    grid_drawer.penup()
    grid_drawer.goto(i, -5)
    grid_drawer.pendown()
    grid_drawer.goto(i, 5)
    grid_drawer.penup()

# Axes
grid_drawer.pencolor("red")
grid_drawer.goto(-5, 0)
grid_drawer.pendown()
grid_drawer.goto(5, 0)
grid_drawer.penup()

grid_drawer.pencolor("blue")
grid_drawer.goto(0, -5)
grid_drawer.pendown()
grid_drawer.goto(0, 5)
grid_drawer.penup()

# Axis Labels + Axis Direction Letters
labeler = turtle.Turtle()
labeler.hideturtle()
labeler.penup()
labeler.speed(0)
labeler.color("black")

# Tick labels
for i in range(-5, 6):
    if i != 0:
        labeler.goto(i, 0.2)
        labeler.write(str(i), align="center", font=("Arial", 8, "normal"))
        labeler.goto(0.3, i)
        labeler.write(str(i), align="left", font=("Arial", 8, "normal"))

# Axis names
labeler.goto(4.5, 0.3)
labeler.write("X", align="center", font=("Arial", 12, "bold"))

labeler.goto(0.3, 4.5)
labeler.write("Y", align="center", font=("Arial", 12, "bold"))
# --- Player Turtle ---
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(1)

#######################################################
# --- Coordinate Guessing Challenge ---
def coordinate_guess_challenge(x, y):
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),          (0, 1),
               (1, -1), (1, 0),  (1, 1)]

    while True:
        valid_positions = [(x + dx, y + dy)
                           for dx, dy in offsets
                           if -5 <= x + dx <= 5 and -5 <= y + dy <= 5]

        if not valid_positions:
            print("🚫 No valid moves left!")
            return x, y

        target_x, target_y = random.choice(valid_positions)

        # Draw challenge dot
        challenge_dot = turtle.Turtle()
        challenge_dot.shape("circle")
        challenge_dot.color("orange")
        challenge_dot.penup()
        challenge_dot.speed(0)
        challenge_dot.goto(target_x, target_y)

        print(f"\n🟠 A dot appeared near you!")
        try:
            guess_x = int(input("👉 Guess the X coordinate of the dot: "))
            guess_y = int(input("👉 Guess the Y coordinate of the dot: "))
        except ValueError:
            print("❌ Please enter valid integers.")
            challenge_dot.hideturtle()
            continue

        if guess_x == target_x and guess_y == target_y:
            print("✅ Correct! Moving turtle to that position.")
            challenge_dot.hideturtle()
            return target_x, target_y
        else:
            print("❌ Try again! That wasn't the right coordinate.")
            challenge_dot.hideturtle()
            time.sleep(1)

def mode_learning():
    x, y = 0, 0
    player.goto(x, y)

    print("\n--------------------------\n🎓 Welcome to Learning Mode!")
    print("Guess the coordinates of the dot near your turtle.")
    print("Get 3 correct in a row to increase difficulty!\n")

    streak = 0
    level = 1  # difficulty level

    while True:
        print(f"\n🐢 Current Position: ({x}, {y})")
        print(f"🧠 Streak: {streak} | 🔢 Difficulty Level: {level} ({(2*level+1)**2 - 1} possibilities)")

        # Generate possible surrounding coordinates based on level
        possibilities = []
        for dx in range(-level, level + 1):
            for dy in range(-level, level + 1):
                if dx == 0 and dy == 0:
                    continue  # skip current location
                new_x = x + dx
                new_y = y + dy
                if -5 <= new_x <= 5 and -5 <= new_y <= 5:
                    possibilities.append((new_x, new_y))

        if not possibilities:
            print("🚫 No valid positions available. Resetting to (0,0)")
            x, y = 0, 0
            player.goto(x, y)
            continue

        # Pick a target
        target_x, target_y = random.choice(possibilities)

        # Draw dot
        challenge_dot = turtle.Turtle()
        challenge_dot.shape("circle")
        challenge_dot.color("orange")
        challenge_dot.penup()
        challenge_dot.speed(0)
        challenge_dot.goto(target_x, target_y)

        # Get user guess
        try:
            guess_x = int(input("👉 Guess the X coordinate of the dot: "))
            guess_y = int(input("👉 Guess the Y coordinate of the dot: "))
        except ValueError:
            print("❌ Please enter valid numbers.")
            challenge_dot.hideturtle()
            continue

        # Check result
        if guess_x == target_x and guess_y == target_y:
            print("✅ Correct! Moving turtle to that position.")
            x, y = target_x, target_y
            player.goto(x, y)
            streak += 1
        else:
            print(f"❌ Nope! The dot was at ({target_x}, {target_y}).")
            streak = 0  # reset streak

        challenge_dot.hideturtle()
        time.sleep(1)

        # Level up every 3 correct
        if streak >= 3:
            level += 1
            streak = 0
            print(f"\n⚡️ Difficulty increased! Now using {(2*level+1)}x{(2*level+1)} grid around you.")
            time.sleep(1)

        # Cap max difficulty based on grid boundary
        if (2 * level + 1) > 11:  # max 11x11 fits grid [-5, 5]
            level = 5

        # exit
        if guess_x == "q"or guess_y == "q":
            print("👋 Goodbye!")
            break 

##########################################
# --- Mode 2: Treasure Hunt ---
##########################################
def mode_treasure():
    x, y = 0, 0
    player.goto(x, y)

    # --- Place treasure ---
    treasure = turtle.Turtle()
    treasure.shape("circle")
    treasure.color("gold")
    treasure.penup()
    treasure.speed(0)
    treasure_x = random.randint(-4, 4)
    treasure_y = random.randint(-4, 4)
    treasure.goto(treasure_x, treasure_y)

    # --- Place traps between turtle and treasure ---
    trap_coords = []
    trap_markers = []

    min_x = min(x, treasure_x)
    max_x = max(x, treasure_x)
    min_y = min(y, treasure_y)
    max_y = max(y, treasure_y)

    attempts = 0
    while len(trap_coords) < 5 and attempts < 50:
        tx = random.randint(min_x, max_x)
        ty = random.randint(min_y, max_y)
        if (tx, ty) not in trap_coords and (tx, ty) != (x, y) and (tx, ty) != (treasure_x, treasure_y):
            trap_coords.append((tx, ty))

            # Draw trap visually
            marker = turtle.Turtle()
            marker.hideturtle()
            marker.penup()
            marker.speed(0)
            marker.goto(tx, ty)
            marker.write("☠️", align="center", font=("Arial", 16, "bold"))
            trap_markers.append(marker)

        attempts += 1

    print("\n--------------------------\n🏴‍☠️ Welcome to Treasure Hunt Mode!")
    print("Avoid traps and find the treasure!")
    print("Use coordinates to move. If you step on ☠️, it's game over.")

    while True:
        print(f"\n🐢 Current Position: ({x}, {y})")
        try:
            new_x = int(input("Enter new X coordinate: "))
            new_y = int(input("Enter new Y coordinate: "))
        except ValueError:
            print("❌ Invalid input. Use whole numbers only.")
            continue

        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            x, y = new_x, new_y
            player.goto(x, y)

            # 🧨 Check for trap
            if (x, y) in trap_coords:
                print("💀 You stepped on a trap... Game Over!")
                player.color("gray")
                break

            # 🎯 Check for treasure
            if x == treasure_x and y == treasure_y:
                print("🏆 You found the treasure! You're a true explorer!")
                player.color("blue")
                break
        else:
            print("🚫 Coordinates out of bounds (-5 to 5). Try again.")

    time.sleep(3)
    screen.bye()

# --- Mode Selection ---
print("🐢 Welcome to Turtle Coordinate Explorer!")
print("Choose your mode:")
print("1️⃣  Learning Mode (Guessing Coordinates)")
print("2️⃣  Treasure Hunt Mode (Move the Turtle)")

while True:
    choice = input("\n--------------------------\nEnter 1 or 2 to select mode: ").strip()
    if choice == "1":
        mode_learning()
        break
    elif choice == "2":
        mode_treasure()
        break
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")
