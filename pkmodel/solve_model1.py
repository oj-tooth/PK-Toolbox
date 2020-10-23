import numpy as np
import scipy.integrate


def dose(t, dose_rate, t_dose):
    '''Test docstring
    '''
    return dose_rate * np.heaviside(t_dose - t, 1)


def rhs(t, y, model):
    #get params out of the model class
    V_c = model.params['V_c']
    CL = model.params['CL']
    k_a = model.params['k_a']
    t_dose = model.params['t_dose']
    dose_rate = model.params['dose_rate']

    #Only using a cenrtal compartment so q_p1 will remain zero.
    if model.compartments == 1:
        Q_p1 = 0
        V_p1 = 1
    else:
        Q_p1 = model.params['Q_p1']
        V_p1 = model.params['V_p1']

    if model.protocol == 'sc':
        q_0, q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dq0_dt = dose(t, dose_rate, t_dose) - k_a * q_0
        dqc_dt = k_a * q_0 - CL * q_c / V_c - transition
        dqp1_dt = transition
        return [dq0_dt, dqc_dt, dqp1_dt]
    elif model.protocol == 'ivb':
        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = dose(t, dose_rate, t_dose) - CL * q_c / V_c - transition
        dqp1_dt = transition
    return [dqc_dt, dqp1_dt]


def initial_conditions(model):
    if model.protocol == 'sc':
        return np.array([0.0, 0.0, 0.0])
    elif model.protocol == 'ivb':
        return np.array([0.0, 0.0])


def solve(model):
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: rhs(t, y, model),
        t_span=[0.0, model.params['t_end']],
        y0=initial_conditions(model),
        rtol=1e-6,
        atol=1e-8
    )
    return sol
