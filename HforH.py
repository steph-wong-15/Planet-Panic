import turtle
import time
import random

##INTRO

print("Welcome to Planet Panic! You will be assigned an object that you must collect, it will be either garbage, recycling, or compost. Your mission is to collect the targets to gain points!")
print("For every 10 points that you get, a pound of garbage will be picked up")
print("Use the keys a,w,s,d to move!")
print("Garbage=RED")
print("Recycling=BLUE")
print("Compost=GREEN")
print("The more you collect, the longer your tail will get! Be sure to avoid the borders and crashing into your own tail!")
mode=input("Please type S for Snake Mode and C for Crocodile Mode")
while mode not in "CcSs":
    mode=input("Type again")
while mode=="C" or mode=="c":
    print("Not available")
    mode=input("Type S")
if mode=="S" or mode=="s":
    print("Let's begin!")

#Time
delay = 0.1

# Score
score = 0
high_score = 0
trees_planted=0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("light green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

#random color
color=""
other1=""
other2=""
numb=random.randint(0, 3)
if numb==1:
    color="red"
    other1="blue"
    other2="green"
if numb==2:
    color="blue"
    other1="red"
    other2="green"
if numb==3:
    color="green"
    other1="blue"
    other2="red"


# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color(color)
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake targ
targ = turtle.Turtle()
targ.shape("square")
targ.speed(0)
targ.color(color)
targ.penup()
targ.goto(100,50)


    
# Snake obs1
obs1 = turtle.Turtle()
obs1.speed(0)
obs1.shape("square")
obs1.color(other1)
obs1.penup()
obs1.goto(50,100)

#Snake obs2
obs2 = turtle.Turtle()
obs2.speed(0)
obs2.color(other2)
obs2.shape("square")
obs2.penup()
obs2.goto(100,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Collected: 0  Most Collected: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
 
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Collected: {}  Most Collected: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()

#Code used from @TokyoEdTech
