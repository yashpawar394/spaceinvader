#to draw frame
import turtle
import os
import math
import turtle
import random
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("space invaders")
 


#to draw frame
frame= turtle.Turtle()
frame.pencolor("white")
frame.speed(0)
frame.penup()
frame.setposition(-300,-300)
frame.pendown()
frame.pensize(4)
for side in range(4):
	frame.fd(600)
	frame.lt(90)
frame.hideturtle()

#set the score
score = 0
# draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
score_pen.hideturtle()

turtle.register_shape('spaceship.gif')	
	
#to draw turtle
player= turtle.Turtle()
player.shape("spaceship.gif")
player.color("blue")
player.penup()
player.speed(0)
player.setposition(0,-270)
player.setheading(90)


playerspeed = 15



#choose the no of enemies
number_of_enemies = 5
#create an empty list of enemies
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
    #to create enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)


enemyspeed = 5
#create playres bullet
bullet = turtle.Turtle()
bullet.color("orange")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 30

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"
def iscollosion(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance< 30:
        return True
    else:
        return False
#to move player
def move_left():
	x  = player.xcor()
	x -= playerspeed
	if x< -280:
		x = -280
	player.setx(x)

def move_right():
        x = player.xcor()
        x += playerspeed
        if x > 280:
                x = 280
        player.setx(x)

def fire_bullet():
    #declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move the bullet to the just above the player
        if bullet.isvisible():
            y= bullet.ycor()+bulletspeed
            bullet.sety(y)
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x, y)
        bullet.showturtle()

    




#create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right,"Right")
turtle.onkeypress(fire_bullet,"space")

#To create mainloop
while True:
    
    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor()> 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor()<-280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        #check for collosion between bullet and enemy
        if iscollosion(bullet,enemy):
            #reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #reset the enemy
            enemy.setposition(-200,250)
            # update score
            score +=10
            scorestring = "score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))


        #check for collosion brtween enemy and player
        if iscollosion(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            False
            break


    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if bullet reaches the top
    if bullet.ycor()> 275:
        bullet.hideturtle()
        bulletstate = "ready"

   
    
    

        
        
    
wn.mainloop()
