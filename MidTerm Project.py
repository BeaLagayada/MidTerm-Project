import turtle
import random

# Setting up Screen
screen = turtle.Screen()
screen.setup(690, 690)
screen.title("Race Game! Player Vs Computer")
screen.bgcolor("cyan")

# Character of the game
# Color Red Player 1
player1 = turtle.Turtle()
player1.color("red")
player1.shape("turtle")
player1.penup()
player1.goto(-200, 80)

# Color Blue Player 2
player2 = player1.clone()
player2.color("blue")
player2.penup()
player2.goto(-200, -100)

# Finish line for the 1st Player
player1.goto(277, 250)
player1.pendown()
player1.right(180)
player1.begin_fill()
player1.color("red")
player1.circle(50, steps=3)
player1.penup()
player1.end_fill()
player1.goto(320, 95)
player1.pendown()
player1.begin_fill()
player1.color("violet")
player1.forward(85.6)
player1.right(90)
player1.forward(80)
player1.right(90)
player1.forward(85.6)
player1.right(90)
player1.forward(80)
player1.penup()
player1.left(90)
player1.end_fill()
player1.penup() #Labelling Player 1 Home
player1.goto(278.5,175)
player1.color("black")
player1.write("PLAYER 1", align = "center", font = ("Arial", 12, "bold"))
player1.color("red")
player1.goto(-200, 100)


# Finish line for the 2nd Player
player2.goto(277, 40)
player2.pendown()
player2.right(180)
player2.begin_fill()
player2.color("blue")
player2.circle(50, steps=3)
player2.penup()
player2.end_fill()
player2.goto(320, -115)
player2.pendown()
player2.begin_fill()
player2.color("pink")
player2.forward(85.6)
player2.right(90)
player2.forward(80)
player2.right(90)
player2.forward(85.6)
player2.right(90)
player2.forward(80)
player2.penup()
player2.left(90)
player2.end_fill()
player2.penup() #Labelling Player 2 Home
player2.goto(278.5,-35)
player2.color("white")
player2.write("PLAYER 2", align = "center", font = ("Arial", 12, "bold"))
player2.color("blue")
player2.goto(-200, -100)

while player1.xcor() < 250 and player2.xcor() < 250:
    # Prompt the player 1 to enter a choice
    print("****************************")
    print("Please Enter a Choice!")
    print("[1] Rock")
    print("[2] Paper")
    print("[3] Scissors")
    print("****************************")
    player1_choice = int(input("Player 1 choose: "))

    # Player 2 randomly chooses
    player2_choice = random.randint(1, 3)
    print("Player 2 choose: ", player2_choice)

    # Determine the Winner for this round
    if player1_choice not in [1, 2, 3]:
        print("Invalid Choice! Please enter 1 for Rock, 2 for Paper, or 3 for Scissors")
    elif player1_choice == player2_choice:
        player1.forward(0)
        player2.forward(0)
    else:
        steps = 50  # Number of steps for a win
        if (
            (player1_choice == 1 and player2_choice == 3)
            or (player1_choice == 2 and player2_choice == 1)
            or (player1_choice == 3 and player2_choice == 2)
        ):
            player1.forward(steps)
        else:
            player2.forward(steps)

# Determine the overall winner
winner = " "
if player1.xcor() >= 250:
    winner = "Player 1 Wins!"
elif player2.xcor() >= 250:
    winner = "Player 2 Wins!"

# Display the winner on the screen
turtle.penup()
turtle.goto(0,0)
turtle.color("black")
turtle.write(winner, align = "center", font = ("Arial", 70, "bold"))

turtle.hideturtle()
turtle.done()





