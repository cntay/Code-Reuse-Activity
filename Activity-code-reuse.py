# -------------------------------------------------
#        Name: Camille, Chidinma, & Jaren
#    Filename: acticity-code-reuse.py
#        Date: July 30, 2019
#
# Description: Siting code
# -------------------------------------------------

#---------------START ATTRIBUTE CODE SECTION--------------------
# Code created with the help of Stack Overflow
# https://stackoverflow.com/questions/25772750/
#
# Question by AlexConfused:
# https://stackoverflow.com/users/3812925/alexconfused
#
# Answer by Kevin:
# https://stackoverflow.com/users/953482/kevin
#
# THE CODE:
import turtle
def draw_sierpinski(length,depth):
    if depth == 0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        t.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)
        
window = turtle.Screen()
t = turtle.Turtle()
draw_sierpinski(100,2)
window.exitonclick()
#----------------END ATTRIBUTE CODE SECTION---------------------

