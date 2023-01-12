###############################################################################
# FILE: quadratic_equation.py
# WRITER:Daniel
# EXCERCISE: intro2cs2 ex2
# a few functions that calculate quadratic equations
###############################################################################
import math

def quadratic_equation(a,b,c):
    """a function that solves a quadratic equation"""
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        solution1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        solution2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        return solution1,solution2
    elif discriminant == 0:
        solution = -b / (2*a)
        return solution, None
    elif discriminant < 0:
        return None, None


def quadratic_equation_user_input():
    """a function that solves a quadratic equation interactively"""
    coeffs = input("Insert coefficients a, b, and c: ")
    #setting the parameters as floats
    a, b, c = coeffs.split()
    a = float(a); b = float(b); c = float(c)
    # this condition checks that 'a' is valid
    if a == 0:
        print("The parameter 'a' may not equal 0")
    else:
        # the next block will print the results accordingly
        solution1, solution2 = quadratic_equation(a, b, c)
        if (solution1 != None) and (solution2 != None):
            print(f"The equation has 2 solutions: {solution1} and "
                  f"{solution2}")
        elif (solution1 != None) and (solution2 == None):
            print(f"The equation has 1 solution: {solution1}")
        else:
            print("The equation has no solutions")

