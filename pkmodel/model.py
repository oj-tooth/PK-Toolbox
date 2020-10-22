#
# Model class
#

class Model:

    def __init__(self, name, params, compartments=0, protocol='ivb'):
        '''

        :param name: name of model
        :type name: string
        :param compartments: number of compartments
        :type compartments: integer
        :param protocol: enter 0 for IVB or 1 for subcutaneous
        :type protocol: integer

        '''

        self.name = name
        self.compartments = compartments
        self.protocol = protocol
        self.params = params


