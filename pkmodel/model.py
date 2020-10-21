#
# Model class
#

class Model:

    def __init__(self, name, compartments=0):
        '''

        :param name: name of model
        :type name: string
        :param compartments: number of compartments
        :type compartments: integer

        '''
        self.name = name
        self.compartments = compartments
