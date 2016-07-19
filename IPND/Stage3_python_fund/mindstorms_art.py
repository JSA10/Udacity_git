import turtle
# find out why called turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100) #move forward 100 spaces/pixels?
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle() 
    brad.shape("turtle")
    brad.color("Green")
    brad.speed(5)

    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
        
    window.exitonclick()
    # closes window when clicked on 

draw_art()
