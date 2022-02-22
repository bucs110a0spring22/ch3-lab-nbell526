import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.forward(55)
leonardo.forward(5)
for x in range(10):
    turtleranges1 = random.randrange(0, 10)
    turtleranges2 = random.randrange(0, 10)
    michelangelo.forward(turtleranges1)
    leonardo.forward(turtleranges2)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

# Part B - complete part B here
leonardo.up()
michelangelo.down()
sides = 3
triangle= (360/sides)
length= 50
for x in range(sides): 
  michelangelo.forward(length)
  michelangelo.left(triangle)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

michelangelo.down()
sides=4
square= (360/sides)
length= 50
for x in range(sides): 
  michelangelo.forward(length)
  michelangelo.left(square)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

michelangelo.down()
sides=6
hexacon= (360/sides)
length= 40
for x in range(sides): 
  michelangelo.forward(length)
  michelangelo.left(hexacon)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

michelangelo.down()
sides=9
nonagon= (360/sides)
length= 30
for x in range(sides): 
  michelangelo.forward(length)
  michelangelo.left(nonagon)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

michelangelo.down()
sides=12
dodecagon= (360/sides)
length= 20
for x in range(sides): 
  michelangelo.forward(length)
  michelangelo.left(dodecagon)
michelangelo.down()
michelangelo.up()
michelangelo.clear()

window.exitonclick()
