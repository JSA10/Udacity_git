import turtle
# find out why called turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    # create a screen / window for turtle to create shapes on

    # initialise a new instance of class turtle, that is able to draw
    #upon all the functions stored in that class
    brad = turtle.Turtle() 
    brad.shape("turtle")
    brad.color("Blue")
    brad.speed(4)
    
    # activate / assign turtle called brad that moves around
    brad.forward(100) #move forward 100 spaces/pixels?
    brad.right(90) #turn right 90 degrees
    brad.forward(100) 
    brad.right(90)
    brad.forward(100) 
    brad.right(90)
    brad.forward(100) 
    brad.right(90)

    # Two turtles!
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.speed(1)
    
    angie.circle(100)
    
    window.exitonclick()
    # closes window when clicked on 

draw_square()
