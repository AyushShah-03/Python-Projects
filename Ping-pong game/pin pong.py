import turtle
import winsound


wn = turtle.Screen()
wn.title('Pong by Ayush')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)                        #Stops the window screen from updating which make things faster

# Paddle A
paddle_a = turtle.Turtle()          # small trutle is module and Turtle is class predefined in turtle itself
paddle_a.speed(0)                   # not a speed of paddle, it is speed of animation so it does not buffer and 0 means max
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.penup()                   #as turtle moves it draws lines, by using this we can remove the line of paddle 
paddle_a.goto(-350, 0)             #cordinate counted from center (0,0)
paddle_a.shapesize(5, 1)           #shape of paddle 5=5times (20*20 px) and 1=default

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('blue')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 0.20                              #dx here d is delta and x is speed on x co-ordinate
ball.dy = 0.20                              #dy here d is delta and y is speed on y co-ordinate

# Pen                                      #Basically it is used to write score
pen = turtle.Turtle()
pen.speed(0)
pen.color('green')
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'bold'))
pen.hideturtle()

# Score
score_a = 0
score_b = 0

def paddle_a_up():                       #function works on moving of paddle_a in upward direction
    y = paddle_a.ycor()                 #.ycor() is from module represents y co-ordinate
    y += 30
    paddle_a.sety(y)                    #sety(y) will set value to new y co-ordinate

def paddle_b_up():                       #function works on moving of paddle_b in upward direction
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_a_down():                       #function works on moving of paddle_a in downward direction
    y = paddle_a.ycor()
    y += -30
    paddle_a.sety(y)

def paddle_b_down():                       #function works on moving of paddle_b in downward direction
    y = paddle_b.ycor()
    y += -30
    paddle_b.sety(y)

# Keyboard binding
wn.listen()                                     #Listen for keyboard input
wn.onkeypress(paddle_a_up, 'w')                 #with W key paddle a will go up
wn.onkeypress(paddle_a_down, 's')               #with S key paddle a will go down
wn.onkeypress(paddle_b_up, 'Up')                #with up key paddle b will go up
wn.onkeypress(paddle_b_down, 'Down')            #with down key paddle b will go down


# Main game loop
while True:
    wn.update()                               #it will start updating window screen

    # Moving Ball
    ball.setx(ball.xcor() + ball.dx)          #Here combining the x last position and with speed and set it in new x
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:                #As the height is 600 so from 0, it will be +-300, placement of ball y co-ordinate 
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)   #Winsound is module and this code will make basic window bounce sound when ball hits surface
        ball.dy *= -1

    if ball.xcor() > 390:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    if ball.xcor() < -390:
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.goto(0, 0)

        ball.dx *= -1
        score_b += 1
        pen.clear()    #IT WILL CLEAR PRVIOUS SCORE
        #used fromat method to print score in turtle
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold')) 
    

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1
        
    # Check if any player has won
    if score_a >= 3:
        print("Player A wins!")
        break
    elif score_b >= 3:
        print("Player B wins!")
        break