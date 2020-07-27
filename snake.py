import turtle
import random

screen = turtle.Screen()

boxDrawer = turtle.Turtle()
boxDrawer.speed(0)

boxDrawer.penup()
boxDrawer.goto(-200, 200)
boxDrawer.pendown()
for i in range(4):
    boxDrawer.forward(400)
    boxDrawer.right(90)
boxDrawer.ht()
    
t = turtle.Turtle()
t.shape('square')
t.penup()
apple = turtle.Turtle()
apple.shape('circle')
apple.penup()
apple.goto(random.randint(-175,175), random.randint(-175,175))

def left():
    t.left(90)

def right():
    t.right(90)

def checkCollision():
    if t.xcor()< -200 or t.xcor() > 200 or t.ycor() < -200 or t.ycor() > 200:
        return True




def direction_status():
    if t.heading() == 90:
        screen.onkey(left, "Left")
        screen.onkey(right, "Right")
    elif t.heading() == 180:
        screen.onkey(left, "Down")
        screen.onkey(right, "Up")
    elif t.heading() == 270:
        screen.onkey(left, "Right")
        screen.onkey(right, "Left")
    else:
        screen.onkey(left, "Up")
        screen.onkey(right, "Down")
    screen.listen()

bodies = []
t_locations = []   
condition = True
while condition:
    t.forward(3)
    t_locations.append((t.xcor(),t.ycor()))
    
    if abs(t.xcor()-apple.xcor())<10 and abs(t.ycor()-apple.ycor())<10:
        apple.goto(random.randint(-175,175), random.randint(-175,175))
        new_bod = turtle.Turtle()
        new_bod.shape('square')
        new_bod.penup()
        bodies.append(new_bod)
        

    #move bodies

    for i in range(len(bodies)-1,-1,-1):
        if i == 0:
            last_t_coord = t_locations[len(t_locations)-2] 
            x=last_t_coord[0]
            y=last_t_coord[1]
            bodies[0].goto(x,y)
        else:
            x = bodies[i - 1].xcor()
            y = bodies[i - 1].ycor()
            bodies[i].goto(x,y)


    for body in bodies:
        if body.xcor()==t.xcor() and body.ycor()==t.ycor():
            print("Game over")
            condition = False
            

    direction_status()

    if checkCollision():
        t.write("Game Over")
        condition = False
