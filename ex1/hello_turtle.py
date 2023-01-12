###############################################################################
# FILE: hello_turtle.py
# WRITER:Daniel
# EXCERCISE: intro2cs2 ex1
# A program that draws three flowers using turtle
###############################################################################
import turtle

def draw_petal():
    """this function draws a petal"""
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

def draw_flower():
    """this function draws an upside down flower"""
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal() 
    # the next two lines draw a stem for the flower
    turtle.left(135)
    turtle.forward(150)

def draw_flower_and_advance():
    """this function draws an upside down flower
     and advances the cursor to allow further drawing"""
    draw_flower() #draws a flower with four petals and a stem
    #the next lines reposition the drawing cursor
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

def draw_flower_bed():
    """this function draws three flowers next to each other"""
    #the next lines reposition the cursor for optimal drawing
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    #the next lines draw the flowers
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()


# the next code below draws three flowers
if __name__ == "__main__":

    draw_flower_bed()

    turtle.done

