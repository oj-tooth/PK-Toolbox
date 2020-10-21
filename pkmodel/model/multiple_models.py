import numpy as np
import scipy.integrate

"""Script to run a model with either IVB or Subcutaneous protocol, either 1 or 2
compartments and constant dose rate.

See documentation of scipy.integrate.solve_ivp for info on solution object.

:return sol: object contatining information about the solution. Specifically sol.t 
is a numpy array with shape (number of timesteps,) containing all the timesteps taken, and
sol.y is a numpy array with shape (2 or 3,number of timesteps) conatining the concentrations of
q_0 (optional in sol.y[0,:]), q_c in sol.y[0(1),:] and q_p1 in sol.y[1(2),:] at each of the timesteps taken.
"""

#until we have bult the model class set protocol manually IVB is 0 and 1 is subcutaneous
protocol = 0 

#input params (eventually make this part of the model class)
dose = 2.0 #this will need to be changed to a function of t also.

CL = 1.0
V_c = 1.0
Q_p1 = 1.0
V_p1 = 1.0

k_a=1.5


def rhs(t, y, Q_p1, V_c, V_p1, CL, k_a):
    """Defines right hand side (rhs) of the ode.

    :param t: Time variable.
    :param y: List containing concentration variables. y[0] is the concentration
    in the central compartment q_c and y[1] is concentration in the peripheral 
    compartment q_p1.
    :param Q_p1: Transition rate between the central and peripheral compartment.
    :param V_c: Volume of the central compartment.
    :param V_p1: Volume of the peripheral compartment.
    :param CL: Clearance rate from the main compartment.
    :param k_a: rate from dosing compartment.
    :return: List of derivatives of q_c, q_p1 and optionally q_0 depending on protocol.
    """
    if protocol == 1:
        q_0, q_c, q_p1 = y
        transition = Q_p1 * (q_c/V_c - q_p1/V_p1)
        dq0_dt =  dose - k_a * q_0
        dqc_dt = k_a * q_0 - CL * q_c/V_c -transition
        dqp1_dt = transition
        return [dq0_dt, dqc_dt, dqp1_dt]
    elif protocol == 0:
        q_c, q_p1 = y
        transition = Q_p1 * (q_c/V_c - q_p1/V_p1)
        dqc_dt = dose - CL * q_c/V_c -transition
        dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

#Define initial condition. This should probably always be 0 and length depends on protocol
if protocol == 1:
    y0 = np.array([0.0, 0.0, 0.0])
elif protocol == 0:
    y0=np.array([0.0, 0.0])
    
#Define time to integrate until.
t_span=[0.0,10.0]

sol = scipy.integrate.solve_ivp(fun=lambda t, y: rhs(t, y, Q_p1, V_c, V_p1, CL, k_a), t_span=t_span, y0=y0)
