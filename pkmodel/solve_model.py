import numpy as np
import scipy.integrate
from model import Model

def rhs(t, y, model):
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
    #get params out of the model class
    
    V_c = model.params['V_c']
    CL = model.params['CL']
    k_a = model.params['k_a']
    dose = model.params['dose']
    if model.compartments == 1:
        Q_p1 = 0
        V_p1 = 1
    else:
        Q_p1 = model.params['Q_p1']
        V_p1 = model.params['V_p1']
    
    if model.protocol == 'sc':
        q_0, q_c, q_p1 = y
        transition = Q_p1 * (q_c/V_c - q_p1/V_p1)
        dq0_dt =  dose - k_a * q_0
        dqc_dt = k_a * q_0 - CL * q_c/V_c -transition
        dqp1_dt = transition
        return [dq0_dt, dqc_dt, dqp1_dt]
    elif model.protocol == 'ivb':
        q_c, q_p1 = y
        transition = Q_p1 * (q_c/V_c - q_p1/V_p1)
        dqc_dt = dose - CL * q_c/V_c -transition
        dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

def initial_conditions(model):
    """Initialises initial conditions for ode solver of correct length 
    using model.protocol attribute.
    """
    if model.protocol == 'sc':
        return np.array([0.0, 0.0, 0.0])
    elif model.protocol == 'ivb':
        return np.array([0.0, 0.0])

#Using a function for this may be slightly redundant
def time_interval(model):
    """initialises t_span from the t_end value in model.params
    for use in the ode solver.
    """
    return [0.0, model.params['t_end']]

def solve(model):
    """See run_model
    """
    sol = scipy.integrate.solve_ivp(fun=lambda t, y: rhs(t, y, model), t_span=time_interval(model), y0=initial_conditions(model))
    return sol



