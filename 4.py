# Method 1
# Using the infinite series 1/(1)^5 - 1/(3)^5 + 1/(5)^5 - 1/(7)^5 + ... = ((pi)^5)*(5/1536)

import numpy as np
import matplotlib.pyplot as plt
Pi = np.pi


initial_approximation_of_formula = 0                          # This will be the value of the formula till n steps
initial_approximations_of_formula = []                        # This will be all of the n steps taken for the formula

for n in range(1, 201):
    initial_approximation_of_formula += (1 / ((2*n-1)**5)) * (-1)**(n+1)
    initial_approximations_of_formula.append(initial_approximation_of_formula)


# Turning to an array to do operations
initial_approximations_of_formula = np.array(initial_approximations_of_formula)

# Getting Pi for the formula
approximations_of_pi = np.power( (initial_approximations_of_formula) * (1536/5) , 0.2)

plt.style.use('fivethirtyeight')
plt.title('1/(1)^2 + 1/(2)^2 + 1/(3)^2 + 1/(4)^2 + ... = ((pi)^2)/6')
plt.axhline(y=Pi, color='red', linewidth=1.5, linestyle='--')
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)
plt.plot(range(1, 201), approximations_of_pi, linewidth=2)
plt.legend()

plt.show()
