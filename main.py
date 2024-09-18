import turtle as T
import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import json



with open("Setting\\Setting.json", 'r') as f:
    data = json.load(f)

Shape = data["Shape"]

def main_menu():
    global MainMenu

    MainMenu = tk.Tk()
    MainMenu.title("PING PONG")
    MainMenu.geometry("500x500")
    MainMenu.resizable(0, 0)

    global Fr1
    Fr1 = tk.Frame(MainMenu, width= 500, height= 500)
    Fr1.pack()
    Fr1.pack_propagate(0)

    Title = tk.Label(Fr1, text= "Ping Pong!", font= ("ROBOTO", 32))
    Title.pack()

    Start = tk.Button(Fr1, text= "Start", font= ("ROBOTO", 16), background = "blue", fg= "White", command= lambda: GamePlay())
    Start.pack()
    Start.place(relx= 0.39, rely= 0.4, width= 120)

    Setting = tk.Button(Fr1, text= "Setting", font= ("ROBOTO", 16), background = "blue", fg= "White", command= lambda: Setting_func())
    Setting.pack()
    Setting.place(relx= 0.39, rely= 0.5, width= 120)
    
    Help = tk.Button(Fr1, text= "How to play", font= ("ROBOTO", 16), background = "blue", fg= "White", command= HowToPlay)
    Help.pack()
    Help.place(relx= 0.39, rely= 0.6, width= 120)


    Quit = tk.Button(Fr1, text= "Quit", font= ("ROBOTO", 16), background = "blue", fg= "White", command= lambda: exit(-1))
    Quit.pack()
    Quit.place(relx= 0.39, rely= 0.7, width= 120)

    MainMenu.mainloop()

def HowToPlay():
    messagebox.showinfo("How to play this game", """
W/Up = go up
S/Down = go down
R = Reset the game
ESC = Quit the game    
                        """)

def Setting_func():
    global MainMenu, Fr1
    global Shape
    global Fr2

    Fr1.pack_forget()
    
    
    Fr2 = tk.Frame(MainMenu, width= 500, height= 500)
    Fr2.pack()
    Fr2.pack_propagate(0)
    
    Ball_shape_label = tk.Label(Fr2, text= "Ball shapes", font=("ROBOTO", 16))
    Ball_shape_label.pack()

    Ball_shape = ttk.Combobox(Fr2, values= ["square", "circle"], font= ("ROBOTO", 16), textvariable= Shape)
    Ball_shape.pack()
    
    if Shape == "circle":
        Ball_shape.current(1)
    elif Shape == "square":
        Ball_shape.current(0)
    
    Apply = tk.Button(Fr2, text= "Apply", font= ("ROBOTO", 16), command= lambda: apply())
    Apply.pack()
    Apply.place(rely = 0.9, relx= 0.8)
    
    Back = tk.Button(Fr2, text= "Back", font= ("ROBOTO", 16), command= lambda: back())
    Back.pack()
    Back.place(rely = 0.9, relx= 0.1)
    
    def apply():
        s = Ball_shape.get()
        data["Shape"] = s
        with open("Setting\\Setting.json", 'w') as f:
            json.dump(data, f)

    def back():
        Fr2.pack_forget()
        Fr1.pack()
        
def GamePlay():
    try:
        # Initialize the main window and ball shape
        global MainMenu, Shape
        MainMenu.destroy()  # Close the main menu window
        Window = T.Screen()  # Create a new Turtle screen for the game
        Window.bgcolor("black")  # Set background color to black
        Window.title("Ping Pong Game")  # Set the window title
        Window.setup(width=800, height=600)  # Set the size of the game window

        # Set up Paddle A (Exercise 13.3 Arrow Keys example from page 4) 
        pad_a = T.Turtle()  # Create a Turtle object for paddle A
        pad_a.speed(0)  # Set speed of animation (0 is the fastest)
        pad_a.shape("square")  # Set shape of paddle A to square
        pad_a.color("white")  # Set color of paddle A to white
        pad_a.shapesize(stretch_wid=5, stretch_len=1)  # Stretch paddle A (wider and shorter)
        pad_a.penup()  # Disable drawing for paddle A
        pad_a.goto(-350, 0)  # Move paddle A to the left side

        # Set up Paddle B (Another example of the same exercise) 
        pad_b = T.Turtle()  # Create a Turtle object for paddle B
        pad_b.speed(0)  # Set speed of animation
        pad_b.shape("square")  # Set shape of paddle B to square
        pad_b.color("white")  # Set color of paddle B to white
        pad_b.shapesize(stretch_wid=5, stretch_len=1)  # Stretch paddle B
        pad_b.penup()  # Disable drawing for paddle B
        pad_b.goto(350, 0)  # Move paddle B to the right side

        # Set up the ball (Linked to 'Bouncing Ball' Task) 
        ball = T.Turtle()  # Create a Turtle object for the ball
        ball.speed(0)  # Set speed of animation
        Shape = data["Shape"]  # Fetch the ball shape from settings
        print(Shape)  # Print shape for debugging purposes
        ball.shape(Shape)  # Set ball shape based on the saved setting
        ball.color("white")  # Set ball color to white
        ball.penup()  # Disable drawing for the ball
        ball.goto(0, 0)  # Position the ball at the center
        ball.dx = 0.05  # Set the horizontal movement of the ball
        ball.dy = 0.05  # Set the vertical movement of the ball

        # Initialize the score variables
        global score_a, score_b
        score_a = 0
        score_b = 0

        # Create a pen object to display the score (Turtle with Text example from Task 6) 
        pen = T.Turtle()  # Create a Turtle object for the score display
        pen.speed(0)  # Set animation speed
        pen.color("white")  # Set pen color to white
        pen.penup()  # Disable drawing
        pen.hideturtle()  # Hide the turtle
        pen.goto(0, 260)  # Position the score display
        pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center", font=("Courier", 24, "normal"))  # Display the score

        # Paddle movement functions (Arrow key binding example from page 4) 
        def pad_a_up():
            y = pad_a.ycor()  # Get the y-coordinate of paddle A
            y += 20  # Move it up by 20 units
            pad_a.sety(y)  # Set the new y-coordinate

        def pad_a_down():
            y = pad_a.ycor()  # Get the y-coordinate of paddle A
            y -= 20  # Move it down by 20 units
            pad_a.sety(y)  # Set the new y-coordinate

        def pad_b_up():
            y = pad_b.ycor()  # Get the y-coordinate of paddle B
            y += 20  # Move it up by 20 units
            pad_b.sety(y)  # Set the new y-coordinate

        def pad_b_down():
            y = pad_b.ycor()  # Get the y-coordinate of paddle B
            y -= 20  # Move it down by 20 units
            pad_b.sety(y)  # Set the new y-coordinate

        # Exit the game (Linked to Scope exercise, where functions control Turtle movement) 
        def ex():
            Window.bye()  # Close the game window

        # Reset the game (Linked to a similar control practice on page 4) 
        def reset():
            global score_a, score_b
            ball.goto(0, 0)  # Reset the ball position to the center
            score_a = 0  # Reset Player A's score
            score_b = 0  # Reset Player B's score
            pen.clear()  # Clear the score display
            pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center", font=("Courier", 24, "normal"))  # Display the reset score

        # Keyboard bindings
        Window.listen()  # Start listening for keyboard input
        Window.onkeypress(pad_a_up, "w")  # Bind W key to move paddle A up
        Window.onkeypress(pad_a_down, "s")  # Bind S key to move paddle A down
        Window.onkeypress(pad_b_up, "Up")  # Bind Up arrow key to move paddle B up
        Window.onkeypress(pad_b_down, "Down")  # Bind Down arrow key to move paddle B down
        Window.onkeypress(ex, "Escape")  # Bind Escape key to exit the game
        Window.onkeypress(reset, "r")  # Bind R key to reset the game

        # Main game loop (Bouncing Ball exercise from page 5) 
        while True:
            Window.update()  # Update the game window every frame
            ball.setx(ball.xcor() + ball.dx * 75)  # Move the ball horizontally
            ball.sety(ball.ycor() + ball.dy * 75)  # Move the ball vertically

            # Ball collision with the top wall (Boundary exercise Task) 
            if ball.ycor() > 290:
                ball.sety(290)  # Reset the ball position
                ball.dy *= -1  # Reverse the ball direction

            # Ball collision with the bottom wall (Another boundary collision handling) 
            if ball.ycor() < -290:
                ball.sety(-290)  # Reset the ball position
                ball.dy *= -1  # Reverse the ball direction

            # Ball goes past paddle B (right side)
            if ball.xcor() > 390:
                score_a += 1  # Increment Player A's score
                ball.goto(0, 0)  # Reset the ball position
                ball.dx *= -1  # Reverse the ball direction
                pen.clear()  # Clear the score display
                pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center", font=("Courier", 24, "normal"))  # Update the score display

            # Ball goes past paddle A (left side)
            if ball.xcor() < -390:
                score_b += 1  # Increment Player B's score
                ball.goto(0, 0)  # Reset the ball position
                ball.dx *= -1  # Reverse the ball direction
                pen.clear()  # Clear the score display
                pen.write("Player A : " + str(score_a) + " Player B : " + str(score_b), align="center", font=("Courier", 24, "normal"))  # Update the score display

            # Ball collision with paddle B (Bouncing example) 
            if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50:
                ball.setx(340)  # Reset the ball position
                ball.dx *= -1  # Reverse the ball direction

            # Ball collision with paddle A (Bouncing example) 
            if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50:
                ball.setx(-340)  # Reset the ball position
                ball.dx *= -1  # Reverse the ball direction
    except Exception:
        pass  # Catch any errors that occur during the game loop

if __name__ == "__main__":
    main_menu()
