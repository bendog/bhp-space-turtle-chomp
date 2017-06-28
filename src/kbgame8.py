#Turtle Graphics Game
import turtle
import math
import random
import os

#Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("kbgame-bg.gif")
wn.tracer(3)

#Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("darkorange")
player.shape("turtle")
player.penup()
player.speed(0)

#create food
maxFoods = 10
foods = []

for count in range(maxFoods):
    foods.append (turtle.Turtle())
    foods[count].color("lightgreen")
    foods[count].shape("circle")
    foods[count].shapesize(.5)
    foods[count].penup()
    foods[count].speed(0)
    foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))

#Set speed variable
speed = 1

#Define  functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def inscreasespeed():
    global speed
    speed += 1

def isCollision(t1, t2):
       d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
       if d < 20:
           return True
       else:
           return False

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(inscreasespeed, "Up")




while True:
    player.forward(speed)

    #Boundary Player Checking x coordinate
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    #Boundary Player Checking y coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(180)
        os.system("afplay bounce.mp3&")

    #Move Food around
    for count in range(maxFoods):
        foods[count].forward(3)

        #Boundary Food Checking x coordinate
        if foods[count].xcor() > 290 or foods[count].xcor() <-290:
           foods[count].right(180)
           os.system("afplay bounce.mp3&")

        #Boundary Food Checking y coordinate
        if foods[count].ycor() > 290 or foods[count].ycor() <-290:
           foods[count].right(180)
           os.system("afplay bounce.mp3&")

        #Collision checking
        if isCollision(player, foods[count]):
           foods[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
           foods[count].right(random.randint(0,360))
           os.system("afplay chomp.mp3&")
















delay = raw_input("Press Enter to finish.")
