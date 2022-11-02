import turtle

def triangle(edge=100):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)

def rectangle(edge=100):
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    turtle.forward(edge)
    turtle.right(90)
    
def circle_sm():
    turtle.circle(10)

def circle_med():
    turtle.circle(25)

def circle_lar():
    turtle.circle(35)

def triangle_sm(edge=20):
    turtle.forward(edge)
    turtle.left(120)
    turtle.forward(edge)
    turtle.left(120)
    turtle.forward(edge)
    turtle.left(120)


#triangle()
#triangle()
#triangle()
#triangle()
#triangle()
#triangle()

rectangle()

circle_med()

circle_lar()

turtle.forward(100)
circle_med()

circle_lar()

turtle.right(90)
turtle.forward(20)
turtle.penup()
turtle.right(90)
turtle.forward(20)
turtle.pendown()
circle_sm()
turtle.penup()
turtle.forward(60)
turtle.pendown()
circle_sm()
turtle.penup()
turtle.forward(20)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(40)
turtle.pendown()
triangle_sm()
turtle.penup()
turtle.forward(60)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.pendown()
turtle.circle(25,180)