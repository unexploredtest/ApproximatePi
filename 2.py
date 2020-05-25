# Method 2
# Using the infinite series 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... = Pi / 4

from functions import *


def operation(n):
    result = (1/(2*n-1)) * (-1)**(n+1)
    return result

def operation_to_pi(n):
    result = 4 * n
    return result

graph_approximations(operation, operation_to_pi, infinte_series='1/1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... = Pi / 4')