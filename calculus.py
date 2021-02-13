import sympy
import regex

# 'x ** 3 * x ** 2'
### TURNING INPUT INTO AN EQUATION
init_term = input("Type your equation: ")

# Adds spaces to help parsing
init_term = f' {init_term} '

# Creates a list of trig functions
functs = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']

# Sets the size of the x axis in the grid
size = 10

line = regex.findall('\s[a-z]\s', init_term)
line = list(dict.fromkeys(line))

for item in line:
    init_term = init_term.replace(item, f" sympy.symbols('{item}') ")
    line.remove(item)

for item in functs:
    init_term = init_term.replace(item, f" sympy.{item}")
    
equation = init_term.replace("' ", "'")
equation = equation.replace(" '", "'")
# , (sympy.symbols('x'), -size, size)
p1 = sympy.plot(eval(equation))

p1