import numpy as np
import scipy.integrate


def dose(t, dose_rate, t_dose):
    """Creates a stepwise dose function.

    For t<t_dose returns the constant value dose_rate.
    For t>t_dose returns 0.

    :param t: current time
    :param t_dose: time to dose at a constant rate until
    :param dose_rate: constant value of dose_rate when t<t_dose
    :return: function of time to be used as forcing in rhs function.
    """
    return dose_rate * np.heaviside(t_dose - t, 1)


def rhs(t, y, model):
    """Defines right hand side (rhs) of the ode.

    :param t: Time variable.
    :param y: List containing concentration variables. The length is dependent
    on the protocol being used.

    For 'ivb': y[0] is the central compartment q_c and y[1] is the peripheral
    q_p1. For 'sc': y[0] is q_0 and y[1] and y[2] contains q_c and q_p1
    respectively.

    If a peripheral compartment is not being used it will still exist but will
    remain identically zero for all time.
    :param Q_p1: Transition rate between the central and peripheral
    compartment.
    :param V_c: Volume of the central compartment.
    :param V_p1: Volume of the peripheral compartment.
    :param CL: Clearance rate from the main compartment.
    :param k_a: Absorption rate for 'sc' dosing.
    :param model: Takes the model class object to retrive input parameters
    from it.
    :return: List of derivatives of q_c, q_p1 and optionally q_0 depending on
    protocol, corresponds to the length of y.
    """
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
    """Creates initial conditions for ode solver of correct length
    depending on the model.protocol being 'ivb' or 'sc'.

    :param model: Model class object which specifies the protocol.
    """
    if model.protocol == 'sc':
        return np.array([0.0, 0.0, 0.0])
    elif model.protocol == 'ivb':
        return np.array([0.0, 0.0])


def solve(model):
    """Uses scipy routine solve_ivp to integrate the appropriate
    coupled first order ode's for a given model from t=0 to t=t_end.
    rhs provides the forcing for the ode's and initial_conditions is
    used to specify the intial concentrations which will usually all
    be zero.

    By default solve_ivp uses the RK45 method, the relative and absolute
    error tolerances (rtol and atol) have been increased to 1e-6 and 1e-8.
    numpy arrays containing the timesteps and solution components of y at
    each timestep are accessed by sol.t and sol.y respectively. For example
    if a 2 compartment 'ivb' model is solved sol.y[0,:] contains the value
    of q_c at each of the timesteps specified by sol.t[:].

    :param model: Model class object to be solved.
    :return sol: Solution object
    """
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: rhs(t, y, model),
        t_span=[0.0, model.params['t_end']],
        y0=initial_conditions(model),
        rtol=1e-6,
        atol=1e-8
    )
    return sol
