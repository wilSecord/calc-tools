from sympy import *
from sympy import symbols
from sympy.plotting import plot
from regex import *

# 'x ** 3 * x + m + m ** 2'
### TURNING INPUT INTO AN EQUATION
init_term = input("Type your equation: ")
init_term = f' {init_term} '

line = findall('\s[a-z]\s', init_term)
print(line)
for item in line:
    init_term = init_term.replace(item, f"symbol('{item}')")
    line.remove(item)
    

equation = init_term.replace(" ", "")
print(equation)
plot(equation)