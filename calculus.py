import sympy
import regex

# Creates a list of trig functions
functs = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']

# # Sets the size of the x axis in the grid
size = 10

# Creates two empty lists. 'equations' and 'final equations' respectively
eqs = []
f_eqs = []

colors = ['r', 'b', 'g', 'y', 'p']
color = 0

# Loops asking for an input until the word 'stop' is put in, regardless of capitals, or until 5 are input.
for i in range(5):
    init_term = input("Input function (this will continue until you type 'stop'): ")
    if init_term.upper() == 'STOP':
        break
    else:
        eqs.append(init_term)


for eq in eqs:

    # Adds spaces to help parsing
    eq = f' {eq} '

    # Searches and creates a list of all variables if typed in properly
    line = regex.findall('\s[a-z]\s', eq)
    
    # Removes duplicates in the list above
    line = list(dict.fromkeys(line))
    
    # For loop to replace all variables with a sympy symbol for parsing
    # i.e. 'x ** 2' -> 'sympy.symbols(' x ')'
    for item in line:
        eq = eq.replace(item, f" sympy.symbols('{item}') ")
    
    # For loop to check with the 'functs' list to replace trig functions with sympy trig functions for parsing
    # i.e. 'sin( x ) ** 2' -> 'sympy.sin(' x ') ** 2'
    for item in functs:
        eq = eq.replace(item, f" sympy.{item}")
        
    # Removes spaces on the inside of the symbols and trig functions
    # i.e. sympy.symbols(' x ') -> sympy.symbols('x')
    equation = eq.replace("' ", "'")
    equation = equation.replace(" '", "'")
    
    # Evaluates the string and turns it into an equation and appends that to the 'final equations' list
    f_eqs.append(eval(equation))

# Creates a variable named 'p1' and has it equal a graph of the first function in the 'final equations' list
p1 = sympy.plot(f_eqs[0], (sympy.symbols('x'), -size, size), ylim=(-size, size), legend=True, show=False)

# Appends the rest of the equations in the 'final equations' list to p1
for eq in f_eqs[1:]:
    p1.extend(sympy.plot(eq, (sympy.symbols('x'), -size, size), ylim=(-size, size), line_color=colors[color], show=False))
    color += 1

# Shows all graphs
p1.show()





















