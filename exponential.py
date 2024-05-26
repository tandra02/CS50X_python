''' Write a program that takes an integer x and prints the result of the (e ** x - 1) formula, where e is a mathematical constant and x 
is the provided integer.For this purpose use the function expm1() defined in the math module. It takes X as an argument and returns the 
result of the formula above.'''

'''Purpose:
The primary purpose of math.expm1() is to provide a more accurate computation for values of x near 0. When x is very small, calculating 
(e ** x − 1) directly using math.exp(x) - 1 can result in a loss of precision due to the limitations of floating-point arithmetic. 
 The math.expm1() function is designed to avoid this loss of precision.'''


import math
print(math.expm1(int(input())))