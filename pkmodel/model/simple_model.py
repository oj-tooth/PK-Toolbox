import numpy as np
import scipy.integrate

"""Script to run intravenous bolus (i.e no q_0) model with central and peripheral
compartment and constant dose rate.

See documentation of scipy.integrate.solve_ivp for info on solution object.

:return sol: object contatining information about the solution. Specifically sol.t 
is a numpy array with shape (number of timesteps,) containing all the timesteps taken, and
sol.y is a numpy array with shape (2,number of timesteps) conatining the concentrations of
q_c in sol.y[0,:] and q_p1 in sol.y[1,:] at each of the timesteps taken.
"""

#input params
dose = 2.0 #this will need to be changed to a function of t also.

CL = 1.0
V_c = 1.0
Q_p1 = 1.0
V_p1 = 1.0


def rhs(t, y, Q_p1, V_c, V_p1, CL):
    """Defines right hand side (rhs) of the ode.

    :param t: Time variable.
    :param y: List containing concentration variables. y[0] is the concentration
    in the central compartment q_c and y[1] is concentration in the peripheral 
    compartment q_p1.
    :param Q_p1: Transition rate between the central and peripheral compartment.
    :param V_c: Volume of the central compartment.
    :param V_p1: Volume of the peripheral compartment.
    :param CL: Clearance rate from the main compartment.
    :return: List of derivatives of q_c and q_p1.
    """
    q_c, q_p1 = y
    transition = Q_p1 * (q_c/V_c - q_p1/V_p1)
    dqc_dt = dose - CL * q_c/V_c -transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

#Define initial condition. This should probably always be 0 concentration in both compartments.
y0 = np.array([0.0, 0.0])

#Define time to integrate until.
t_span=[0.0,10.0]


sol = scipy.integrate.solve_ivp(fun=lambda t, y: rhs(t, y, Q_p1, V_c, V_p1, CL), t_span=t_span, y0=y0)
