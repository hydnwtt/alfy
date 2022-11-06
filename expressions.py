import math
#Basic Calculator
def calc_math_expression(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator not in ["+", "-", "*", "/"]:
        return None
    else:
        return None

def calc_math_expression_from_str(str_input):
    string = str_input.split()
    num_1 = float(string[0])
    num_2 = float(string[1])
    op1 = string[2]
    return(calc_math_expression(num_1, num_2, op1))

#Largest and Smallest Numbers
def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    num_list = [num1, num2, num3]
    maxmin = (max(num_list), min(num_list))
    return maxmin

#Quadratic equation solver
def quadratic_equation_solver(a,b,c):
    discriminant = ((b*b) - (4*a*c))
    if discriminant < 0:
        return (None, None)
    elif discriminant == 0:
        s1 = ((-b) / (2*a))
        return (s1, None)
    else:
        s1 = ((-b) + math.sqrt(discriminant)) / (2*a)
        s2 = ((-b) - math.sqrt(discriminant)) / (2*a)
        return (s1, s2)

def quadtratic_equation_solver_from_user_input(inputs):
    inputs_list = inputs.split()
    input_1 = inputs_list[0]
    input_2 = inputs_list[1]
    input_3 = inputs_list[2]
    if input_1 = 0:
        print("'A' cannot be equal to zero")
    elif len(inputs_list) > 3:
        print("You can only submit three numbers")
    elif len(inputs_list) < 3:
        print("You must submit three numbers")
    else:
        return quadratic_equation_solver(input_1, input_2, input_3)



#Temp Checker
def temp_checker(min_temp, temp_1, temp_2, temp_3):
    day_temp = [temp_1, temp_2, temp_3]
    count = 0
    for temp in day_temp:
        if temp > min_temp:
            count += 1
    if count >= 2:
        return True
    else:
        return False