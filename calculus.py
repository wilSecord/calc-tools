from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# x**3 + 2*x**2
function = input()
output = ''
alf = 'abcdefghijklmnopqrstuvwxyz'
ucircle_f = ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']
s = 40

def to_symbols(fnctn):
    global output
    for item in fnctn:
        if item in alf:
            if item in ucircle_f:
                pass
            else:
                output += f"symbols('{item}')"
        else:
            output += item
    return output

output = to_symbols(function)

print(diff(output))

fig = plt.figure(figsize= (10, 10))

x = np.linspace(-s, s, 10000)
y = diff(output)

plt.grid()
plt.xlim(-s, s)
plt.ylim(-s, s)
plt.plot(x, y)

plt.show()