# Method 1
# Using the infinite series 1/(1)^2 + 1/(2)^2 + 1/(3)^2 + 1/(4)^2 + ... = ((pi)^2)/6

from functions import *


def operation(n):
    result = (1 / (n**2))
    return result

def operation_to_pi(n):
    result = np.sqrt( (n) * 6 )
    return result

graph_approximations(operation, operation_to_pi, infinte_series='1/(1)^2 + 1/(2)^2 + 1/(3)^2 + 1/(4)^2 + ... = ((pi)^2)/6')