import sympy
import regex

# 'x ** 3 * x ** 2'

### TURNING INPUT INTO AN EQUATION
# Grabbing an input
init_term = input("Type your equation: ")

# Adds spaces to help parsing
init_term = f' {init_term} '

# Creates a list of trig functions
functs = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']

# Sets the size of the x axis in the grid
size = 10

# Searches and creates a list of all variables if typed in properly
line = regex.findall('\s[a-z]\s', init_term)

# Removes duplicates in the list above
line = list(dict.fromkeys(line))

# For loop to replace all variables with a sympy symbol for parsing
for item in line:
    init_term = init_term.replace(item, f" sympy.symbols('{item}') ")

# For loop to check with the 'functs' list to replace trig functions with sympy trig functions for parsing
for item in functs:
    init_term = init_term.replace(item, f" sympy.{item}")
    
# Removes spaces on the inside of the symbols and trig functions
# i.e. sympy.symbols(' x ') -> sympy.symbols('x')
equation = init_term.replace("' ", "'")
equation = equation.replace(" '", "'")

### PLOTTING
# Creates the p1 variable as a plot function
#               Turns the string into a parsable equation
#                    |           
#                    |           Sets the x plane size
#                    |                           |
#                    V                           V
p1 = sympy.plot(eval(equation), (sympy.symbols('x'), -size, size))

# Runs the plot function
p1