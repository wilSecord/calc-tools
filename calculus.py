import sympy
import regex

# Creates a list of trig functions
functs = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']

# Sets the size of the x axis in the grid
size = 30

# Creates 4 empty lists.
d_eqs = [] # 'derivative equations'
f_d_eqs = [] # 'final derivative equations'
eqs = [] # 'equations'
f_eqs = [] # 'final equations'

# Creates a list of the color names used by the plotting function in sympy
colors = ['r', 'b', 'g', 'y', 'c']

# Creates an integer that will determine the color of each of the mathematical functions
color = 0

# Creates a function that sets the equation up for solving later.
def solve_eq(equation):
    
    # Adds spaces to help parsing
    equation = f' {eq} '

    # Searches and creates a list of all variables if typed in properly
    line = regex.findall('\s[a-z]\s', eq)
    
    # Removes duplicates in the list above
    line = list(dict.fromkeys(line))
    
    # For loop to replace all variables with a sympy symbol for parsing
    # i.e. 'x ** 2' -> 'sympy.symbols(' x ')'
    for item in line:
        equation = eq.replace(item, f" sympy.symbols('{item}') ")
    
    # For loop to check with the 'functs' list to replace trig functions with sympy trig functions for parsing
    # i.e. 'sin( x ) ** 2' -> 'sympy.sin(' x ') ** 2'
    for item in functs:
        equation = equation.replace(item, f" sympy.{item}")
        
    # Removes spaces on the inside of the symbols and trig functions
    # i.e. sympy.symbols(' x ') -> sympy.symbols('x')
    equation = equation.replace("' ", "'")
    equation = equation.replace(" '", "'")
    
    return equation
    
# Creates a function that makes a plot with given list and title and plots all equations in given list
def create_plot(list, plt_title):
    global color
    plt = sympy.plot(list[0], (sympy.symbols('x'), -size, size), ylim=(-size, size), legend=True, show=False, title=plt_title)
    for eq in list[1:]:
        plt.extend(sympy.plot(eq, (sympy.symbols('x'), -size, size), ylim=(-size, size), line_color=colors[color], show=False))
        
        # Increases the 'color' integer by 1 to change the color of the next mathematical function
        color += 1
    return plt

# Prints the basic instructions of the program
print('''
      For this calculator to work properly, it requires specific syntax
      Spaces must be put around every number/variable/function
      Example: x ** 3 - sin( x ) ** 2
      
      If you would like to take the derivative of the equation,
      put 'd/dx' at the beginning with the equation in perentheses
      Example: d/dx( x ** 2 * x )
      ''')

# Loops asking for an input until the word 'stop' is put in, regardless of capitals, or until 5 are input.
for i in range(5):
    init_term = input("Input function (this will continue until you type 'stop'): ")
    if init_term.upper() == 'STOP':
        break
    elif init_term.startswith('d/dx'):
        # Takes the derivative equation, removes the prefix, and adds it to the list 'derivative equations'
        init_term = init_term.replace('d/dx', '')
        d_eqs.append(init_term)
    else:
        # Adds the equation to the list 'equations'
        eqs.append(init_term)

    # Solves all equations in the 'equations list and adds them to the 'final equations' list
for eq in eqs:
    equation = solve_eq(eq)
    f_eqs.append(equation)
    
# Solves all equations in the 'derivative equations' list and adds them to the 'final derivative equations' list
for eq in d_eqs:
    equation = solve_eq(eq)
    equation = sympy.diff(eval(equation))
    f_d_eqs.append(equation)
    

if len(f_eqs) > 0: # If the amount of equations in 'final equations' is greater than 0, 
    # create a plot under variable p1, titled: "Equations", with all equations graphed on it
    p1 = create_plot(f_eqs, "Equations")
        
if len(f_d_eqs) > 0: # If the amount of equations in 'final derivative equations' is greater than 0, 
    # create a plot under variable p2, titled: "Derivatives", with all derivative equations graphed on it
    p2 = create_plot(f_d_eqs, "Derivatives")

# Shows all graphs
p1.show()
p2.show()