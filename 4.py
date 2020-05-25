# Method 1
# Using the infinite series 1/(1)^5 - 1/(3)^5 + 1/(5)^5 - 1/(7)^5 + ... = ((pi)^5)*(5/1536)

from functions import *

def operation(n):
    result = (1 / ((2*n-1)**5)) * (-1)**(n+1)
    return result

def operation_to_pi(n):
    result = np.power( (n) * (1536/5) , 0.2)
    return result

graph_approximations(operation, operation_to_pi, infinte_series='1/(1)^5 - 1/(3)^5 + 1/(5)^5 - 1/(7)^5 + ... = ((pi)^5)*(5/1536)')
