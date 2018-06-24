import turtle

def draw_square(brad):
    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")
    
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("red")
    brad.speed(6)

    for i in range(0, 19):
        draw_square(brad)
        brad.right(20)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue");
    angie.circle(100)

    triangle = turtle.Turtle()
    triangle.shape("triangle")
    triangle.color("blue")
    triangle.speed(8)
    
    for i in range(0, 3):
        triangle.forward(160)
        triangle.right(120)

    window.exitonclick()


draw_art()
