import numpy as np
import sympy as sp
#from IPython.display import Markdown, display
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def population_change_dt(N_pop,t, rate_pop_change):
    """
    Model population change
    :param N: the population at the beginning of the time step
    :param k: the growth rate
    :return: the change in population
    """
    dN_popdt = rate_pop_change * N_pop
    return dN_popdt

N_pop_0 = 8700000 #Initial population
rate_pop_change = 0.006 #Growth rate simplified as constant
t = np.arange(2024, 2051, 1)

#Solve the differential equation
solution_pop = odeint(population_change_dt, N_pop_0, t, args=(rate_pop_change,))


# Plotting the solution
def plot(rate_pop_change):
    solution = odeint(population_change_dt, N_pop_0, t, args=(rate_pop_change,))
    plt.plot(t, solution_pop, label='Population Growth')
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.legend()
    plt.grid(True)
    plt.show()

plot(rate_pop_change)

print("Population at each time step:")
for i in range(len(t)):
    print(f"Year: {t[i]:.2f}, Population: {solution_pop[i][0]:.1f}")

growth_at_each_step = np.diff(solution_pop.flatten())  # Taking the difference between consecutive population values

print("Population growth at each time step:", growth_at_each_step)

def Cement_use_MFH_dt(N_MFH_units, t, rate_MFH_change, M_concrete_use_MFH, person_per_unit, share_MFH):
    """
    Model MFH cement use change
    :param N_MFH_units: Number of MFH units
    :param t: time [y]
    :param rate_MFH_change: rate of change in MFH units
    :param M_concrete_use_MFH: concrete use for MFH [tonnes/year]
    :param person_per_unit: average number of people per MFH unit
    :param share_MFH: share of MFH units in total units
    :return: the change in MFH cement use
    """
    growth_at_each_step = np.diff(odeint(population_change_dt, N_pop_0, np.array([t, t + 1]), args=(rate_pop_change,)).flatten())
    housing_need = growth_at_each_step / person_per_unit
    M_concrete_per_MFH = M_concrete_use_MFH / N_MFH_units
    dMFHdt = housing_need * share_MFH * rate_MFH_change * M_concrete_per_MFH
    return dMFHdt

N_MFH_0 = 37441  # Initial number of newly built MFH units in 2015
person_per_unit = 2.2  # Average number of people per MFH unit
rate_MFH_change = 1.006  # Growth rate of MFH units
M_concrete_use = 408000000  # Concrete use in 2015
share_MFH = 0.86  # Share of MFH units in total units

# Solve the differential equation for MFH cement use change
solution_MFH = odeint(Cement_use_MFH_dt, N_MFH_0, t, args=(rate_MFH_change, M_concrete_use, person_per_unit, share_MFH))

# Plotting the solution NOTE: PLOTTING THIS DOESNT REALLY MAKES SENSE - DELETE!!
def plot(rate_MFH_change):
    solution = odeint(Cement_use_MFH_dt, N_MFH_0, t, args=(rate_MFH_change, M_concrete_use, person_per_unit, share_MFH))
    plt.plot(t, solution_MFH, label='MFH Cement Use')
    plt.xlabel('Time')
    plt.ylabel('Cement Use')
    plt.legend()
    plt.grid(True)
    plt.show()

plot(rate_MFH_change)


Cement_use_MFH_at_each_time_step = np.diff(solution_MFH.flatten())  # Taking the difference between consecutive population values
print("Cement use at each time step:", Cement_use_MFH_at_each_time_step)

print("Cement use at each time step:")
for i in range(len(t)):
    print(f"Year: {t[i]:.2f}, Cement Use: {solution_MFH[i][0]:.1f}")


