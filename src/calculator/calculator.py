"""This module contains the calculator functions for the formulas square, tri, lazy caterer, and magic squares"""


def squareNums(n):
    """Calculates the square"""
    return n**2


def triNums(n):
    """Calculates the tri number"""
    return (n * (n + 1)) / 2


def lazyCaterer(n):
    """Calculates the lazy caterer number"""
    return (n**2 + n + 2) / 2


def magicSquares(n):
    """Calculates the magic squares number"""
    return (n * (n**2 + 1)) / 2


def add(a, b):
    return a + b


def multiply(a, b): 
    return a * b


def hypotenuse(a, b):
    """Calculates the hypotenuse of a right triangle"""
    return (a**2 + b**2)**0.5


def run_calculator_one(input_formula, input_num1):
    """Calls and returns results for the specified formulas"""
    calculator = [squareNums, triNums, lazyCaterer, magicSquares]
    formula = calculator[input_formula - 1]
    return_result = formula(input_num1)
    return return_result


def run_calculator_two(input_formula, input_num1, input_num2):
    """Calls and returns results for the specified formulas"""
    calculator = [squareNums, triNums, lazyCaterer, magicSquares, add, multiply, hypotenuse]
    formula = calculator[input_formula - 1]
    return_result = formula(input_num1, input_num2)
    return return_result


if __name__ == "__main__":
    print(
        "Choose which formula to use: 1 for square, 2 for tri, 3 for lazy caterer, 4 for magic squares, " + 
        "5 for add, 6 for multiplication, 7 for hypotenuse of a right triangle"
    )
    input_formula = int(input())
    if input_formula in [1, 2, 3, 4]:
        print("Enter a number to calculate the square, tri, lazy caterer, and magic squares numbers")
        input_num = int(input())

        result = run_calculator_one(input_formula, input_num)
        print(result)
    else:
        print("Enter two numbers to add, multiply or calculate the hypotenuse of a right triangle")
        input_num1 = int(input())
        input_num2 = int(input())

        result = run_calculator_two(input_formula, input_num1, input_num2)
        print(result)
