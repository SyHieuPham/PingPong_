<h1>IST ASSESSMENT</h1>
<section>
    <h2>Sy Hieu Pham - 10IST1</h2>
</section>

<h2>Introduction</h2>
<p>
This Ping Pong game is a simple Python project using turtle and tkinter. The game includes a main menu with options to start, adjust settings, view controls, or quit. Players control paddles using the keyboard, with Player A using W and S, and Player B using the arrow keys. The ball bounces off the walls, and points are scored when a player misses. Settings allow the ball shape to be changed between a square and a circle. The game features reset and quit functions and keeps track of player scores.</p>


<h2>Code explanation</h2>

```markdown
# Ping Pong Game

## Functions Explained

### `main_menu()`

The `main_menu()` function is the first screen that appears when you start the game. It creates a window with the title "PING PONG" and several buttons. These buttons allow you to start the game, go to the settings, see how to play, or quit the game. 

In this function:
- The `Start` button starts the game.
- The `Setting` button opens the settings menu where you can change the ball shape.
- The `How to play` button shows a popup with the game controls.
- The `Quit` button closes the game.

### `HowToPlay()`

The `HowToPlay()` function opens a message box that tells the player how to control the paddles:
- `W` and `S` keys to move the left paddle (Player A).
- `Up Arrow` and `Down Arrow` keys to move the right paddle (Player B).
- `R` to reset the game.
- `ESC` to quit.

### `Setting_func()`

The `Setting_func()` function opens the settings menu. In this menu, you can change the shape of the ball to either a square or a circle. When you click the "Apply" button, the selected shape is saved in the `Setting.json` file, so it is remembered the next time you play. 

In this function:
- You can choose the ball shape using a dropdown menu.
- You can go back to the main menu by clicking "Back".
- The "Apply" button saves your selected settings.

### `GamePlay()`

The `GamePlay()` function starts the actual Ping Pong game. It creates the window where the game is played. The paddles and ball are drawn on the screen, and the game begins. 

In this function:
- Player A controls the left paddle with the `W` and `S` keys.
- Player B controls the right paddle with the `Up Arrow` and `Down Arrow` keys.
- The ball bounces around, and the players try to stop it from going past their paddles.
- Scores are updated whenever a player misses the ball.
- The `R` key resets the game, and the `ESC` key quits the game.

### `apply()`

The `apply()` function is inside the `Setting_func()` and is used to save your chosen ball shape to the `Setting.json` file. After you select either "circle" or "square" from the dropdown menu and click "Apply," this function updates the settings.

### `back()`

The `back()` function is also part of the `Setting_func()`. It simply takes you back to the main menu by hiding the settings screen and showing the main menu again.

### `pad_a_up()` and `pad_a_down()`

These functions control the movement of the left paddle (Player A). 
- `pad_a_up()` moves the left paddle up by 20 units.
- `pad_a_down()` moves the left paddle down by 20 units.

### `pad_b_up()` and `pad_b_down()`

These functions control the movement of the right paddle (Player B).
- `pad_b_up()` moves the right paddle up by 20 units.
- `pad_b_down()` moves the right paddle down by 20 units.

### `ex()`

The `ex()` function allows you to quit the game by closing the game window.

### `reset()`

The `reset()` function resets the game by setting the ball back to the middle of the screen and resetting both players' scores to 0.

---

This explanation covers the main functions in the game and what they do. Each function has a specific purpose, like starting the game, moving paddles, or updating settings.
```

<h2>Code, Linking</h2>
```python
import turtle as T #Import turtle library
import random #Import random library
import tkinter as tk #Import tkinter for creading GUI
from tkinter import ttk #Import tkk from tkinter
from tkinter import messagebox #Import messagebox for tell player what they should do
import threading #Import threading for run multiple threat in 1 program
import json #Import json library for reading json file

#Open json file name setting for read
with open("Setting\\Setting.json", 'r') as f:
    data = json.load(f)

#Set this variable name Shape save the Shape what player change in setting function
Shape = data["Shape"]

#Main menu
def main_menu():
    #Make it global so I can call it in any function
    global MainMenu

    #Set MainMenu is a GUI
    MainMenu = tk.Tk()
    MainMenu.title("PING PONG")
    MainMenu.geometry("500x500")
    MainMenu.resizable(0, 0)

    #Fr1 is a name of a Frame in GUI
    global Fr1
    Fr1 = tk.Frame(MainMenu, width= 500, height= 500)
    Fr1.pack()
    Fr1.pack_propagate(0)

    #Title is a label
    Title = tk.Label(Fr1, text= "Ping Pong!", font= ("ROBOTO", 32))
    Title.pack()

    #Start button
    Start = tk.Button(Fr1, text= "Start", font= ("ROBOTO", 16), background = "blue", fg= "White", command= lambda: GamePlay())
    Start.pack()
    Start.place(relx= 0.39, rely= 0.4, width= 120)

    #Setting Button, show setting GUI
    Setting = tk.Button(Fr1, text= "Setting", font= ("ROBOTO", 16), background = "blue", fg= "White", command= lambda: Setting_func())
    Setting.pack()
    Setting.place(relx= 0.39, rely= 0.5, width= 120)

    #Help Button, Show what key player can use
    Help = tk.Button(Fr1, text= "How to play", font= ("ROBOTO", 16), background = "blue", fg= "White", command= HowToPlay)
    Help.pack()
    Help.place(relx= 0.39, rely= 0.6, width= 120)

    #Quit button
    Quit = tk.Button(Fr1, text= "Quit", font= ("ROBOTO", 16), background = "blue", fg= "White", command= lambda: exit(-1))
    Quit.pack()
    Quit.place(relx= 0.39, rely= 0.7, width= 120)

    #Make Menu run
    MainMenu.mainloop()

#Show player message box about game's key
def HowToPlay():
    messagebox.showinfo("How to play this game", """
W/Up = go up
S/Down = go down
R = Reset the game
ESC = Quit the game
    """)

#Setting function, make a GUI and then player can customize it
def Setting_func():
    #call other variable in this function
    global MainMenu, Fr1
    global Shape
    global Fr2

    #Destroy the before frame
    Fr1.pack_forget()
    
    #Create a new frame
    Fr2 = tk.Frame(MainMenu, width= 500, height= 500)
    Fr2.pack()
    Fr2.pack_propagate(0)

    #Label of the setting
    Ball_shape_label = tk.Label(Fr2, text= "Ball shapes", font=("ROBOTO", 16))
    Ball_shape_label.pack()

    #A box where player can change ball shape
    Ball_shape = ttk.Combobox(Fr2, values= ["square", "circle"], font= ("ROBOTO", 16), textvariable= Shape)
    Ball_shape.pack()

    #Check what in setting
    if Shape == "circle":
        Ball_shape.current(1)
    elif Shape == "square":
        Ball_shape.current(0)

    #Apply button
    Apply = tk.Button(Fr2, text= "Apply", font= ("ROBOTO", 16), command= lambda: apply())
    Apply.pack()
    Apply.place(rely = 0.9, relx= 0.8)

    #Go back button
    Back = tk.Button(Fr2, text= "Back", font= ("ROBOTO", 16), command= lambda: back())
    Back.pack()
    Back.place(rely = 0.9, relx= 0.1)

    #Apply function, Save everything player customize in the game to the json file
    def apply():
        s = Ball_shape.get() #Get the text box
        data["Shape"] = s #Set value of the data
        #dump file
        with open("Setting\\Setting.json", 'w') as f:
            json.dump(data, f)

    #Go back function
    def back():
        Fr2.pack_forget()
        Fr1.pack()
        
def GamePlay():
    try:
        global MainMenu, Shape #call the global variable
        MainMenu.destroy() #Destroy the main menu
        Window = T.Screen() #Create a screen for turtle in page 
        Window.bgcolor("black")
        Window.title("Ping Pong Game")
        Window.setup(width= 800, height= 600)

        pad_a= T.Turtle()
        pad_a.speed(0)
        pad_a.shape("square")
        pad_a.color("white")
        pad_a.shapesize(stretch_wid=5,stretch_len=1)
        pad_a.penup()
        pad_a.goto(-350,0)

        pad_b= T.Turtle()
        pad_b.speed(0)
        pad_b.shape("square")
        pad_b.color("white")
        pad_b.shapesize(stretch_wid=5,stretch_len=1)
        pad_b.penup()
        pad_b.goto(350,0)

        ball= T.Turtle()
        ball.speed(0)
        Shape = data["Shape"]
        print(Shape)
        ball.shape(Shape)
        ball.color("white")
        ball.penup()
        ball.goto(0,0)
        ball.dx = 0.05
        ball.dy = 0.05

        global score_a, score_b
        score_a = 0
        score_b = 0

        pen = T.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0,260)
        pen.write("Player A : "+ str(score_a) +" Player B : "+ str(score_b),align="center",font=("Courier",24,"normal"))

        def pad_a_up():
            y = pad_a.ycor()
            y += 20
            pad_a.sety(y)   

        def pad_a_down():
            y = pad_a.ycor()
            y -= 20
            pad_a.sety(y)

        def pad_b_up():
            y = pad_b.ycor()
            y += 20
            pad_b.sety(y)   

        def pad_b_down():
            y = pad_b.ycor()
            y -= 20
            pad_b.sety(y)  

        def ex():
            Window.bye()
            

        def reset():
            global score_a, score_b
            ball.goto(0, 0)
            score_a = 0
            score_b = 0
            pen.clear()
            pen.write("Player A : "+ str(score_a) +" Player B : "+ str(score_b),align="center",font=("Courier",24,"normal"))

        Window.listen()
        Window.onkeypress(pad_a_up,"w")
        Window.onkeypress(pad_a_down,"s")
        Window.onkeypress(pad_b_up,"Up")
        Window.onkeypress(pad_b_down,"Down")
        Window.onkeypress(ex, "Escape")
        Window.onkeypress(reset, "r")

        while True:
            Window.update()
            ball.setx(ball.xcor() + ball.dx * 75)
            ball.sety(ball.ycor() + ball.dy * 75)
            
            if ball.ycor() > 290 :
                ball.sety(290)
                ball.dy *= -1
            
            if ball.ycor() < -290 :
                ball.sety(-290)
                ball.dy *= -1
            
            if ball.xcor() > 390 :
                score_a += 1
                ball.goto(0,0)
                ball.dx *= -1
                pen.clear()
                pen.write("Player A : "+ str(score_a) +" Player B : "+ str(score_b),align="center",font=("Courier",24,"normal"))
            
            if ball.xcor() < -390 :
                score_b += 1
                ball.goto(0,0)
                ball.dx *= -1
                pen.clear()
                pen.write("Player A : "+ str(score_a) +" Player B : "+ str(score_b),align="center",font=("Courier",24,"normal"))

            
            if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50 :
                ball.setx(340)
                ball.dx *= -1

            if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50 :
                ball.setx(-340)
                ball.dx *= -1
    except Exception:
        pass

if __name__ == "__main__":
    main_menu()
```
