#
# Model class
#

class Model:

    def __init__(self, name, compartments=0, protocol=0):
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
        self.params = {
            'Q_p1': 1.0,
            'V_c': 1.0,
            'V_p1': 1.0,
            'CL': 1.0,
            'k_a': 1.5,
            'dose': 2.0,
            't_end': 10.0
        }
#For now I have just put in some sample parameters we can discuss tomorrow
#the best way for a user to enter these. I added dose which for now is just a
# constant as well as t_end for the integration - Joe.