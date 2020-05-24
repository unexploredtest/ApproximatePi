# Method 1
# Using the infinite series 1/(1)^2 + 1/(2)^2 + 1/(3)^2 + 1/(4)^2 + ... = ((pi)^2)/6

from functions import *

# initial_approximation_of_formula = 0                          # This will be the value of the formula till n steps
# initial_approximations_of_formula = []                        # This will be all of the n steps taken for the formula

# for n in range(1, 201):
#     initial_approximation_of_formula += (1 / (n**2))
#     initial_approximations_of_formula.append(initial_approximation_of_formula)


# # Turning to an array to do operations
# initial_approximations_of_formula = np.array(initial_approximations_of_formula)

# # Getting Pi for the formula
# approximations_of_pi = np.sqrt( (initial_approximations_of_formula) * 6 )

# plt.style.use('fivethirtyeight')
# plt.title('1/(1)^2 + 1/(2)^2 + 1/(3)^2 + 1/(4)^2 + ... = ((pi)^2)/6')
# plt.axhline(y=Pi, color='red', linewidth=1.5, linestyle='--', label='Pi')
# plt.axhline(y=0, color='black', linewidth=1)
# plt.axvline(x=0, color='black', linewidth=1)
# plt.plot(range(1, 201), approximations_of_pi, linewidth=2)
# plt.legend()

# plt.show()

graph_approximations(lambda x: (1 / (x**2)), lambda x: np.sqrt( (x) * 6 ))