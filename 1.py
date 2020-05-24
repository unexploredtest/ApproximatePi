# Method 1
# Using the formula 1/(1)^2 + 1/(2)^2 + 1/(3)^2 + 1/(4)^2 + ... = ((pi)^2)/6

import numpy as np
import matplotlib.pyplot as plt
Pi = np.pi


initial_approximation_of_formula = 0
initial_approximations_of_formula = []

for n in range(1, 201):
    initial_approximation_of_formula += (1 / (n**2))
    initial_approximations_of_formula.append(initial_approximation_of_formula)


initial_approximations_of_formula = np.array(initial_approximations_of_formula)

approximations_of_pi = np.sqrt( (initial_approximations_of_formula) * 6 )

# plt.style.use('fivethirtyeight')
# plt.axhline(y=Pi, color='red', linewidth=1.5, linestyle='--')
# plt.axhline(y=0, color='black', linewidth=1)
# plt.axvline(x=0, color='black', linewidth=1)
# plt.plot(range(1, 201), approximations_of_pi, linewidth=2)

# plt.show()
for num in approximations_of_pi:
    print(num)