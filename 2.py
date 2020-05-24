# Method 2
# Using the infinite series 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... = Pi / 4

import numpy as np
import matplotlib.pyplot as plt
Pi = np.pi


initial_approximation_of_formula = 0                          # This will be the value of the formula till n steps
initial_approximations_of_formula = []                        # This will be all of the n steps taken for the formula

for n in range(1, 21):
    initial_approximation_of_formula += (1/(2*n-1)) * (-1)**(n+1)
    initial_approximations_of_formula.append(initial_approximation_of_formula)


# Turning to an array to do operations
initial_approximations_of_formula = np.array(initial_approximations_of_formula)

# Getting Pi for the formula
approximations_of_pi = initial_approximations_of_formula * 4

plt.style.use('fivethirtyeight')
plt.title('1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... = Pi / 4')
plt.axhline(y=Pi, color='red', linewidth=1.5, linestyle='--')
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)
plt.plot(range(1, 21), approximations_of_pi, linewidth=2)
plt.legend()

plt.show() 
