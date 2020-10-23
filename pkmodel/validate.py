
def validate_params(params):
    """For each model parameter, checks if they are all floating point numbers and if not, raises an error.
       :param params: Set of Model class object parameters
    """
    for key in params:
        if (type(params[key]) is not float):
            if (type(params[key]) is not int):
                if params[key] is not None:
                    raise TypeError('All parameters should be floating point numbers (e.g. 1.0). Parameter ' + key + ' is not.')
        if params[key] is not None:
            if params[key] <= 0.:
                raise ValueError('Values must all be greater than 0')


def validate_protocol(protocol):
    """Takes in protocol input and checks if it corresponds
    to the 'ivb' (intravenous bolus) or 'sc' (subcutaneous)
    model options. If not, returns an error.
    """
    if protocol not in ['ivb', 'sc']:
        raise ValueError("Protocol must be 'ivb' or 'sc'")


def validate_compartments(compartments):
    """Takes in number of model compartments as input and
    checks if it is an integer or is negative. If not the function
    raises errors.
    """
    if (type(compartments) is not float):
        if (type(compartments) is not int):
            raise TypeError('Number of compartments should be a floating point number (e.g. 2.0)')
    if compartments <= 0.:
        raise ValueError('Number of compartments must be 1 or more')


def validate_name(name):
    """Takes in name of model as input and checks if it is a string.
    If not, raises TypeError.
    """
    if type(name) is not str:
        raise TypeError('Name must be a string')


def validate(name, params, compartments, protocol):
    """Takes in model name, parameters, compartments and protocol
    and validates each argument using the appropriate function.
    """
    validate_params(params)
    validate_protocol(protocol)
    validate_compartments(compartments)
    validate_name(name)