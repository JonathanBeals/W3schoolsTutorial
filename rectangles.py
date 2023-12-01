import turtle, random, time


# Get user's name
user_name = input("Enter your name: ")

# Get turtle choice
print("Choose a turtle to bet on:")
print("1 - Turtle 1")
print("2 - Turtle 2")
print("3 - Turtle 3")
print("4 - Turtle 4")
print("5 - Turtle 5")

turtle_choice = int(input("Choose a Turtle. 1-5: "))


#Print Turtle Race.
def print_word(word, x, y, font=("Arial", 48, "bold")):
    tess.color("white", "black")
    tess.penup()
    tess.goto(x, y)
    tess.write(word, align="center", font=font)
    tess.hideturtle()

keke = turtle.Turtle()

#Print Turtle Number.
def print_number(word, x, y, font=("Arial", 32, "bold")):
    keke.color("white", "black")
    keke.penup()
    keke.goto(x, y)
    keke.write(word, align="center", font=font)
    keke.hideturtle()

# Set up tess
tess = turtle.Turtle()
tess.color("black")
tess.pensize(3)
tess.speed(10)
tess.penup()
tess.speed(1000)
wn = turtle.Screen()
wn.setup(1400,700)
turtle.bgpic("background.gif")
print_word("Turtle Race!!", 0, 270)
tess.left(90)
tess.hideturtle()


#Bring window to the front
rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

#Set up alex
alex = turtle.Turtle()
alex.color("white", "sienna3")
alex.pensize(3)
alex.penup()
alex.speed(10)
wn = turtle.Screen()
wn.setup(1400,700)
alex.goto(-700, -205)
alex.hideturtle()

# Function to draw a rectangle
def draw_rectangle():
    alex.pendown()
    alex.begin_fill()
    for _ in range(2):
        alex.forward(1500)
        alex.left(90)
        alex.forward(80)
        alex.left(90)
    alex.end_fill()

# Function to draw track
def draw_track():
    for _ in range(5):
        draw_rectangle()
        alex.penup()
        alex.goto(-700, alex.ycor() + 83)

# Draw track
draw_track()


print_number("1", -660, 140)
print_number("2", -660, 60)
print_number("3", -660, -25)
print_number("4", -660, -110)
print_number("5", -660, -190)


def draw_square(size, color):
    for i in range(4):
        tess.forward(20)
        tess.right(90)

def draw_checkerboard_line(turtle, color1, color2, x, y1, y2, num_squares):
    turtle.penup()
    turtle.goto(x, y1)

    for i in range(num_squares):
        if i % 2 == 0:
            turtle.color(color1)
        else:
            turtle.color(color2)

        turtle.pendown()
        turtle.begin_fill()
        for b in range(4):
            turtle.forward(20)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(20)



# Draw start line
draw_checkerboard_line(tess, "black", "white", -600, -200, 300, 20)
draw_checkerboard_line(tess, "white", "black", -580, -200, 300, 20)

# Draw finish line
draw_checkerboard_line(tess, "black", "white", 640, -200, 300, 20)
draw_checkerboard_line(tess, "white", "black", 620, -200, 300, 20)


# Create turtles
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle4 = turtle.Turtle()
turtle5 = turtle.Turtle()

# Setup turtles
def setup_turtle(turtle, color, start_pos):
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(start_pos)
    turtle.start_pos = start_pos

# Define starting positions for each turtle
start_positions = {
    "turtle1": (-640, 172),
    "turtle2": (-640, 85),
    "turtle3": (-640, 0),
    "turtle4": (-640, -85),
    "turtle5": (-640, -172)}

# Call setup_turtle() with the start positions
setup_turtle(turtle1, "deepskyblue", start_positions["turtle1"])
setup_turtle(turtle2, "mediumpurple", start_positions["turtle2"])
setup_turtle(turtle3, "black", start_positions["turtle3"])
setup_turtle(turtle4, "crimson", start_positions["turtle4"])
setup_turtle(turtle5, "slategrey", start_positions["turtle5"])

# Function to check if a turtle has reached the stop point
def has_reached_stop_point(turtle, stop_point_x):
    return turtle.xcor() >= stop_point_x

def race(turtle1, turtle2, turtle3, turtle4, turtle5, stop_point_x):
    while True:
        turtle1.forward(random.randint(0, 40))
        turtle2.forward(random.randint(0, 40))
        turtle3.forward(random.randint(0, 40))
        turtle4.forward(random.randint(0, 40))
        turtle5.forward(random.randint(0, 40))

        # Check if any turtle has reached the stop point
        if any(has_reached_stop_point(t, stop_point_x)
            for t in [turtle1, turtle2, turtle3, turtle4, turtle5]):
                break

# Define a function to execute a race segment
def race_segment(turtle1, turtle2, turtle3, turtle4, turtle5, stop_point_x):
    while True:
        turtle1.forward(random.randint(0, 40))
        turtle2.forward(random.randint(0, 40))
        turtle3.forward(random.randint(0, 40))
        turtle4.forward(random.randint(0, 40))
        turtle5.forward(random.randint(0, 40))

        if any(has_reached_stop_point(t, stop_point_x) for t in [turtle1, turtle2, turtle3, turtle4, turtle5]):
            break

# Define a function to display the winner message
def display_winner(message):
    print_word(message, 0, -40)

# Define the reset_race() function
def reset_race(turtles):
    for turtle in turtles.values():
        turtle.goto(turtle.start_pos)


# Create turtles dictionary
turtles = {
    "turtle1": turtle1,
    "turtle2": turtle2,
    "turtle3": turtle3,
    "turtle4": turtle4,
    "turtle5": turtle5
}

reset_race(turtles)

# Set up the stop point
stop_point_x = 630

def clear_screen()


while True:
    if clear_screen:
        wn.clear()

    race_segment(turtle1, turtle2, turtle3, turtle4, turtle5, stop_point_x)  # Run a race segment

    winning_turtle = None
    for i, turtle in enumerate([turtle1, turtle2, turtle3, turtle4, turtle5], 1):
        if has_reached_stop_point(turtle, stop_point_x):
            winning_turtle = i
            break

    # Check if the user's turtle wins
    user_wins = (winning_turtle == turtle_choice)
    if user_wins:
        winner_message = f"Congrats, {user_name}! Your turtle won!"
    else:
        winner_message = f"The Winner is Turtle # {winning_turtle}."

    display_winner(winner_message)  # Display winner and wait for user input

    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("Thank you for playing!")
        wn.bye()  # Close the turtle window
        break  # Exit the loop to close the window
    else:
        reset_race(turtles)  # Reset the race setup
        # Display the winner again if needed
        print_word(winner_message, 0, -40)

    # Set the flag to True after the first race
    clear_screen = True