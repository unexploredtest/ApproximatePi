import numpy as np
import matplotlib.pyplot as plt
Pi = np.pi


# This will calculate the values of the series from first to the n'th term
def vlaue_of_n_steps(operation, n_start=1, n_end=200):
    initial_approximation_of_infinite_series = 0                          # This will be the value of the infinite_series till n steps
    initial_approximations_of_infinite_series = []                        # This will be all of the n steps taken for the infinite_series

    # This will add the n'th term to the value
    for n in range(n_start, n_end+1):
        initial_approximation_of_infinite_series += operation(n)
        # Saving the new value
        initial_approximations_of_infinite_series.append(initial_approximation_of_infinite_series)

    return initial_approximations_of_infinite_series


# After using the infinte series, we translate it to Pi
def approximation_of_n_steps(operation, operation_to_pi, n_start=1, n_end=200):
    results_of_infinite_series = vlaue_of_n_steps(operation, n_start, n_end)
    # Changing the list to an array to do operation effeciently 
    results_of_infinite_series = np.array(results_of_infinite_series)
    Pi_approximations = operation_to_pi(results_of_infinite_series)
    return Pi_approximations


# Graphing the approximations
def graph_approximations(operation, operation_to_pi, n_start=1, n_end=200, infinte_series=''):
    Pi_approximations = approximation_of_n_steps(operation, operation_to_pi, n_start, n_end)

    plt.style.use('fivethirtyeight')
    plt.title(infinte_series)
    plt.axhline(y=Pi, color='red', linewidth=1.5, linestyle='--', label='Pi')
    plt.axhline(y=0, color='black', linewidth=1)
    plt.axvline(x=0, color='black', linewidth=1)
    plt.plot(range(1, 201), Pi_approximations, linewidth=2)
    plt.legend()

    plt.show()




