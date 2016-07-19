import turtle
# find out why called turtle

def draw_square_circle_triangle():
    window = turtle.Screen()
    window.bgcolor("red")
    # create a screen / window for turtle to create shapes on

    # initialise a new instance of class turtle, that is able to draw
    #upon all the functions stored in that class
    brad = turtle.Turtle() 
    brad.shape("turtle")
    brad.color("Blue")
    brad.speed(2)
    
    # activate / assign turtle called brad that moves around
    square = (1,2,3,4)
    for i in square:
        brad.forward(100) #move forward 100 spaces/pixels?
        brad.right(90) #turn right 90 degrees

    # Two turtles!
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("green")
    angie.speed(4)
    
    angie.circle(100)

    # Three turtles
    tel = turtle.Turtle()
    tel.shape("classic")
    tel.color("black")

    triangle = (1,2,3)
    for i in triangle:
        tel.forward(100) #move forward 100 spaces/pixels?
        tel.right(120) #turn right 60 degrees
        tel.speed(3)
        
    window.exitonclick()
    # closes window when clicked on 

draw_square_circle_triangle()
