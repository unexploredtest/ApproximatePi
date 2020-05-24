# Method 3
# Using the infinite series 2/1 * 2/3 * 4/3 * 4/5 * 6/5 * 6/7 * ... = Pi / 2

import numpy as np
import matplotlib.pyplot as plt
Pi = np.pi


initial_approximation_of_formula = 1                          # This will be the value of the formula till n steps
initial_approximations_of_formula = []                        # This will be all of the n steps taken for the formula

odd_value = 1
even_vlaue = 0
for n in range(1, 21):
    if n % 2 == 0:
        odd_value += 2
    else:
        even_vlaue += 2
    initial_approximation_of_formula *= (even_vlaue)/(odd_value)
    initial_approximations_of_formula.append(initial_approximation_of_formula)


# Turning to an array to do operations
initial_approximations_of_formula = np.array(initial_approximations_of_formula)

# Getting Pi for the formula
approximations_of_pi = initial_approximations_of_formula * 2

plt.style.use('fivethirtyeight')
plt.title('2/1 * 2/3 * 4/3 * 4/5 * 6/5 * 6/7 * ... = Pi / 2')
plt.axhline(y=Pi, color='red', linewidth=1.5, linestyle='--')
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)
plt.plot(range(1, 21), approximations_of_pi, linewidth=2)
plt.legend()

plt.show() 
