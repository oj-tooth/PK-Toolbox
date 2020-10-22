def validate_params(params):
    for key in params:
        if (type(params[key]) is not float):
            if (type(params[key]) is not int):
                raise TypeError('All parameters should be floating point numbers (e.g. 1.0). Parameter ' + key + ' is not.')
        if params[key] <= 0.:
            raise ValueError('Values must all be greater than 0')


def validate_protocol(protocol):
    if protocol not in ['ivb', 'sc']:
        raise ValueError("Protocol must be 'ivb' or 'sc'")


def validate_compartments(compartments):
    if (type(compartments) is not float):
        if (type(compartments) is not int):
            raise TypeError('Number of compartments should be a floating point number (e.g. 2.0)')
    if compartments <= 0.:
        raise ValueError('Number of compartments must be 1 or more')


def validate_name(name):
    if type(name) is not str:
        raise TypeError('Name must be a string')


def validate(name, params, compartments, protocol):
    validate_params(params)
    validate_protocol(protocol)
    validate_compartments(compartments)
    validate_name(name)
