import sympy
import re

functs = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']

size = 30

d_eqs = []
f_d_eqs = []
eqs = []
f_eqs = []

colors = ['r', 'b', 'g', 'y', 'c']

color = 0

class Equation:
    def __init__(self, eq):
        self.eq = eq
    
    def parse(self):
        equation = f' {self.eq} '
        line = re.findall('\W[a-z]\W', equation)
        line = list(dict.fromkeys(line))
        
        for item in line:
            item = re.sub('\W', '', item)
            equation = equation.replace(item, f"sympy.symbols('{item}')")
        
        for item in functs:
            if item in equation:
                equation = equation.replace(item, f'sympy.{item}')
        
        equation = equation.replace(' ', '')
        equation = str(equation)
        return equation
         
    
class Plot:
    def __init__(self, lst, plt_title):
        self.lst = lst
        self.plt_title = plt_title
        
    def plot(self):
        
        global color
        # for eq in self.lst:
        #     print(eq)      
        
        print(self.lst[0])
        plt = sympy.plotting.plot(eval(str(self.lst[0])),
                     (sympy.symbols('x'), -size, size),
                     ylim=(-size, size),
                     legend=True, show=False,
                     title=self.plt_title)
    
        for eq in self.lst[1:]:
            print(eq)
            plt2 = sympy.plotting.plot(eval(str(eq)),
                        (sympy.symbols('x'), -size, size), 
                        ylim=(-size, size),
                        line_color=colors[color],
                        show=False)
            
            plt.extend(plt2)
            
            color += 1
        return plt

if __name__ == '__main__':
    for i in range(5):
        
        init_term = input("Input function (this will continue until you type 'stop'): ")
        
        if init_term.upper() == 'STOP':
            break
        elif init_term.startswith('d/dx'):
            init_term = init_term.replace('d/dx', '')
            f_d_eqs.append(Equation(sympy.diff(eval(str(Equation(init_term).parse())))).parse())
        else:
            f_eqs.append(str(Equation(init_term).parse()))
        
    if len(f_eqs) > 0:
        p1 = Plot(f_eqs, 'Equations').plot()

    if len(f_d_eqs) > 0:
        p2 = Plot(f_d_eqs, 'Derivatives').plot()
        
    if f_eqs != []:
        p1.show()
    
    if f_d_eqs != []:
        p2.show()