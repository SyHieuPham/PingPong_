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
        global MainMenu, Shape
        MainMenu.destroy()
        Window = T.Screen()
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
