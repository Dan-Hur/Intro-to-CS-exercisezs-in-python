###############################################################################
# FILE: calculate_mathematical_expression.py
# WRITER:Daniel
# EXCERCISE: intro2cs2 ex2 
# A few functions for basic calculations
###############################################################################

def calculate_mathematical_expression(num1,num2,operation):
    """this function applies an operation between two numbers"""
    result = 0
    if operation in "+-/*":
        # the next block will apply the calculations
        if operation == "+":
            result = num1 + num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            if num2 == 0:
                return None
            else:
                result = num1 / num2
    else:
        return None

    return result

def calculate_from_string(equation):
    """this function calculates the result of an equation from a string"""
    seperated_string = equation.split()
    num1 = float(seperated_string[0])
    num2 = float(seperated_string[2])
    operator = seperated_string[1]
    return calculate_mathematical_expression(num1, num2, operator)

