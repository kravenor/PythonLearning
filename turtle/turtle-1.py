import turtle 
col = ('red', 'yellow', 'pink', 'cyan', 'green', 'white')
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor('black')
t.speed(25)
for i in range(250):
    t.color(col[i % 6])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)
