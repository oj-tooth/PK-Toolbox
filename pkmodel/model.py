#
# Model class
#
from . import validate


class Model:

    def __init__(self, name, params, compartments=0, protocol='ivb'):
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
        validate.validate(name, params, compartments, protocol)
        self.name = name
        self.compartments = compartments
        self.protocol = protocol
        self.params = params
