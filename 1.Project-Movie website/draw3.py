# -*- coding: cp936 -*-
import turtle

def draw_quadrilateral(brad):
    brad.forward(100)
    brad.right(60)
    brad.forward(100)
    brad.right(120)
    brad.forward(100)
    brad.right(60)
    brad.forward(100)

def draw_flower():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(16)

    brad.pu()
    brad.setpos(-200, 20)
    brad.pd()

    for i in range(0, 37):
        draw_quadrilateral(brad)
        brad.right(10)

    brad.left(160)
    brad.forward(220)


def draw_angle(brad, l, start_degree):
    brad.begin_fill()
    brad.color("blue","green")
    brad.right(start_degree)
    for i in range(0, 3):
        brad.forward(l)
        brad.right(120)

    brad.end_fill()
        
    
def draw_triangle(brad, x, y, l):
    brad.pu()
    brad.setpos(x, y)
    brad.pd()
    
    draw_angle(brad, l, 60)
    brad.right(60)
    brad.forward(l)
    brad.left(60)
    draw_angle(brad, l, 0)
    brad.left(60)
    brad.forward(l)
    draw_angle(brad, l, 60)

def draw_3_triangle(x, y, l):
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue")
    brad.speed(2)
    
    draw_triangle(brad, x, y, l)
    #draw_triangle(brad, x-l/2, y-l/2, l)
    #draw_triangle(brad, x+l/2, y-l/2, l)
    
    
def draw_line():
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue")
    brad.speed(2)

    # k
    brad.right(90)
    brad.forward(130)
    
    brad.pu()
    brad.setpos(65, 0)
    brad.pd()
    
    brad.right(45)
    brad.forward(90)

    brad.left(90)
    brad.forward(90)

    # o
    brad.pu()
    brad.setpos(120, 0)
    brad.pd()

    brad.right(135)
    brad.forward(40)

    brad.left(90)
    brad.forward(130)

    brad.left(90)
    brad.forward(40)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")
    window.screensize(1000,800)

    #draw_flower()
    #draw_triangle(100,20)
    draw_3_triangle(0, 0, 30)
    #draw_line()
    
    window.exitonclick()


draw_art()
