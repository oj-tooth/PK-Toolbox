import numpy as np
import scipy.integrate


def dose(t, dose_rate, t_dose):
    '''
    Model class object containing the model name and various parameters.
    Takes mandatory arguments name and params and optional arguments
    compartments and protocol.

    :param name: name of model
    :type name: string
    :param compartments: number of compartments
    :type compartments: integer
    :param protocol: enter 'ivb' for IVB or 'sc' for subcutaneous
    :type protocol: integer
    
    '''

    return dose_rate * np.heaviside(t_dose - t, 1)
