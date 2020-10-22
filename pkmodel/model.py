#
# Model class
#
def validate(name, params, compartments, protocol):
    for key in params:
        if (type(params[key]) is not float):
            if (type(params[key]) is not int):
                raise TypeError('All parameters should be floating point numbers (e.g. 1.0). Parameter ' + key + ' is not.')
        if params[key]<=0.:
            raise ValueError('Values must all be greater than 0')

    if protocol not in ['ivb','sc']:
        raise ValueError("Protocol must be 'ivb' or 'sc'")
    if (type(compartments) is not float):
        if (type(compartments) is not int):
            raise TypeError('Number of compartments should be a floating point number (e.g. 2.0)')
    if compartments<=0:
        raise ValueError('Number of compartments must be 1 or more')
    if type(name) is not str:
        raise TypeError('Name must be a string')

class Model:

    def __init__(self, name, params, compartments=0, protocol='ivb'):
        '''

        :param name: name of model
        :type name: string
        :param compartments: number of compartments
        :type compartments: integer
        :param protocol: enter 'ivb' for IVB or 'sc' for subcutaneous
        :type protocol: integer

        '''
        validate(name, params, compartments, protocol)
        self.name = name
        self.compartments = compartments
        self.protocol = protocol
        self.params = params

        




    


