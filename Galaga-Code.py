#Import Statements
import turtle as trtl
#import time
import time
#import random
import random


#Definining/storage

wn = trtl.Screen()
wn.setup(864,864)
wn.title("Galaga by Roman and Tristan")
wn.bgpic("background.gif")
wn.register_shape("player.gif")
wn.register_shape("enemy.gif")

#Game Functions
score = 0
bullets = []
enemies = []
screen = trtl.Screen()

p1 = trtl.Turtle(shape = "player.gif")
p1.penup()
p1.goto(0, -250)
p1.setheading(90)  # Point upwards
p1.speed(0)


# Function to create enemies
def create_enemies():
    for _ in range(5):
        enemy = trtl.Turtle(shape = "enemy.gif")
        enemy.penup()
        enemy.goto(random.randint(-380, 380), random.randint(100, 250))
        enemies.append(enemy)




#setup
create_enemies()

# Create score display
score_display = trtl.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 300)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Game over display
game_over_display = trtl.Turtle()
game_over_display.speed(0)
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)

# Timer display
timer_display = trtl.Turtle()
timer_display.speed(0)
timer_display.color("white")
timer_display.penup()
timer_display.hideturtle()
timer_display.goto(350, 260)

# Timer variables
time_limit = 15
start_time = time.time()


# Movement functions
def move_left():
    x = p1.xcor()
    if x > -380:
        p1.setx(x - 20)


def move_right():
    x = p1.xcor()
    if x < 380:
        p1.setx(x + 20)



# Function to shoot bullets

def shoot():
    bullet = trtl.Turtle()
    bullet.shape("circle")
    bullet.shapesize(.5)
    bullet.color("white")
    bullet.penup()
    bullet.speed(0)
    bullet.goto(p1.position())
    bullet.setheading(90)  # Point upwards
    bullets.append(bullet)


# Function to move bullets
def move_bullets():
    for bullet in bullets:
        y = bullet.ycor()
        bullet.sety(y + 35)





# Function to check for collisions
def check_collisions():
    global score
    for bullet in bullets:
        for enemy in enemies:
            if bullet.distance(enemy) < 20:
                bullet.hideturtle()
                enemy.hideturtle()
                bullets.remove(bullet)
                enemies.remove(enemy)


                # Increase score
                score += 1
                score_display.clear()
                score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
                break


# Function to check game over
def check_game_over():
    if time.time() - start_time > time_limit:
        if enemies:  # If there are still enemies left
            game_over_display.write("Game Over", align="center", font=("Courier", 36, "normal"))
            return True
        else:
            return False  # No enemies left, game continues
    return False





# Function to update the timer display
def update_timer():
    remaining_time = time_limit - (time.time() - start_time)
    timer_display.clear()
    timer_display.write(f"Time: {int(remaining_time)}", align="right", font=("Courier", 24, "normal"))


# Function to move bullets
def move_bullets():
    for bullet in bullets:
        y = bullet.ycor()
        bullet.sety(y + 20)

# Function to move enemies
def move_enemies():
    for enemy in enemies:
        y = enemy.ycor()
        enemy.sety(y - 3)

# Function to check for collisions
def check_collisions():
    global score
    for bullet in bullets:
        for enemy in enemies:
            if bullet.distance(enemy) < 20:
                bullet.hideturtle()
                enemy.hideturtle()
                bullets.remove(bullet)
                enemies.remove(enemy)

                # Increase score
                score += 1
                score_display.clear()
                score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
                break

# Function to check game over
def check_game_over():
    if time.time() - start_time > time_limit:
        if enemies:  # If there are still enemies left
            game_over_display.write("Game Over", align="center", font=("Courier", 36, "normal"))
            return True
    return False

# Function to update the timer display
def update_timer():
    remaining_time = time_limit - (time.time() - start_time)
    timer_display.clear()
    timer_display.write(f"Time: {int(remaining_time)}", align="right", font=("Courier", 24, "normal"))

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(shoot, "space")

# Main game loop
while True:
    screen.update()
    move_bullets()
    move_enemies()
    check_collisions()
    update_timer()

    # Check if all enemies are defeated
    if not enemies:  # If all enemies have been defeated
        create_enemies()  # Create new enemies
        start_time = time.time()  # Reset the timer for the new wave

    # Check if the game is over based on time limit
    if check_game_over():
        game_over_display.write("Game Over", align="center", font=("Courier", 36, "normal"))
        break  # Exit the loop if the game is over

    # Add a delay to control the game speed
    time.sleep(0.02)




wn.mainloop()