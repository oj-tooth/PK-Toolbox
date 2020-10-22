#
# Model class
#
import validate


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
        validate.validate(name, params, compartments, protocol)
        self.name = name
        self.compartments = compartments
        self.protocol = protocol
        self.params = params
