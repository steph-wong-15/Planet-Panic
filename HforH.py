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
targ.speed(0)
targ.shape("square")
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
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

pen.goto(0,100)
pen.write("Welcome to Planet Panic", align="center", font=("Courier", 36, "bold"))
pen.goto(0,0)
    
# Main game loop
while True:
    wn.update()
    
    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Collected: {}  Most Collected: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(targ) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        targ.goto(x,y)
        obs1.goto(random.randint(-290, 290),random.randint(-290, 290))
        obs2.goto(random.randint(-290, 290),random.randint(-290, 290))

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(color)
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Collected: {}  Most Collected: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    if head.distance(obs1)<20 or head.distance(obs2)<20:
        score=score-1
        obs1.goto(random.randint(-290, 290),random.randint(-290, 290))
        obs2.goto(random.randint(-290, 290),random.randint(-290, 290))
        pen.clear()
        pen.write("Collected: {}  Most Collected: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
        
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Collected: {}  Most Collected: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()

