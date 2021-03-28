import sympy
import re
import logging as lg

lg.basicConfig(level=lg.DEBUG)

functs = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']

size = 30

d_eqs = []
f_d_eqs = []
eqs = []
f_eqs = []

colors = ['r', 'b', 'g', 'y', 'c']

color = 0

def parse(equation): 
    
    equation = f' {equation} '
    line = re.findall('\W[a-z]\W', equation)
    line = list(dict.fromkeys(line))
    
    for item in line:
        item = re.sub("\W", "", item)
        equation = equation.replace(item, f"sympy.symbols('{item}')")
        
    for item in functs:
        if item in equation:
            equation = equation.replace(item, f"sympy.{item}")
    
    equation = equation.replace(" ", "")
    lg.debug(equation)
    lg.debug(eval(equation))
    
    return equation

def plot(lst, plt_title):
    
    global color
    for eq in lst:
        eq = eq.replace("**", "^")
    
    plt = sympy.plot(eval(str(lst[0])),
                     (sympy.symbols('x'), -size, size),
                     ylim=(-size, size),
                     legend=True, show=False,
                     title=plt_title)
    
    for eq in lst[1:]:
        plt.extend(sympy.plot(eval(str(eq)),
                              (sympy.symbols('x'), -size, size),
                              ylim=(-size, size),
                              line_color=colors[color],
                              show=False))
        color += 1
    return plt

for i in range(5):
        
        init_term = input("Input function (this will continue until you type 'stop'): ")
        
        if init_term.upper() == 'STOP':
            break
        elif init_term.startswith('d/dx'):
            init_term = init_term.replace('d/dx', '')
            d_eqs.append(init_term)
            print(init_term)
        else:
            eqs.append(init_term)
    
for eq in eqs:
    f_eqs.append(parse(eval(str(parse(eq)))))

for eq in d_eqs:
    f_d_eqs.append(parse(sympy.diff(eval(str(parse(eq))))))

if len(f_eqs) > 0:
    p1 = plot(f_eqs, "Equations")

if len(f_d_eqs) > 0:
    p2 = plot(f_d_eqs, "Derivatives")
    
if f_eqs == []:
    pass
else:
    p1.show()    

if f_d_eqs == []:
    pass
else:
    p2.show()