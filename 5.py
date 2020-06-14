# Method 1
# Using the infinite series 1/(1)^5 - 1/(3)^5 + 1/(5)^5 - 1/(7)^5 + ... = ((pi)^5)*(5/1536)

from functions import *
from math import factorial

def operation(n):
    result = ((factorial(n))**2)*(2**n)/(factorial(2*n + 1))
    return result

def operation_to_pi(n):
    result = 2 * n
    return result

print(approximation_of_n_steps(operation, operation_to_pi, n_start=0, n_end=100))
# graph_approximations(operation, operation_to_pi, n_start=0, n_end=10)
