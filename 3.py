# Method 3
# Using the infinite series 2/1 x 2/3 x 4/3 x 4/5 x 6/5 x 6/7 x ... = Pi / 2

from functions import *


def operation(n):
    if n % 2 == 0:
        even_value = n
        odd_value = n+1
    else:
        even_value = n+1
        odd_value = n
 
    result = (even_value)/(odd_value)
    return result

def operation_to_pi(n):
    result = 2 * n
    return result

graph_approximations(operation, operation_to_pi, product=True, infinte_series='2/1 x 2/3 x 4/3 x 4/5 x 6/5 x 6/7 x ... = Pi / 2')