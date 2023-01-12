###############################################################################
# FILE: shapes.py
# WRITER:Daniel
# EXCERCISE: intro2cs2 ex2
#a few functions for calculating shapes
###############################################################################
import math
PI = math.pi

def circle_area(radius):
    area = PI * radius**2
    return area

def rectangle_area(side1,side2):
    area = side1 * side2
    return area

def triangle_area(side):
    """calculates the area of equilateral triangle"""
    area = (math.sqrt(3) / 4) * math.pow(side,2)
    return area

def shape_area():
    """this function calculates three types of areas chosen by the user"""
    shape = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if shape not in "123":
        return None
    elif shape == '1':
        radius = float(input())
        return circle_area(radius)
    elif shape == '2':
        side1 = float(input())
        side2 = float(input())
        return rectangle_area(side1,side2)
    else:
        side = float(input())
        return triangle_area(side)
