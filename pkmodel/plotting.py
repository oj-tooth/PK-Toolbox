import matplotlib.pyplot as plt


def figure_creator(model_list, sol_list):
    '''
    figure_creator takes an input of a list of Model class objects
    and a list of solution objects and outputs a plot of drug
    quantities in each compartment versus time.

    :param model_list: A list of model class instances
    :type model_list: list
    :param sol: an list of objects (sol) containing:
        sol.t, an array of timesteps;
        and sol.y, an array of the ODE solutions
    :type sol: list
    :return fig: visualisation of solutions to model(s)
    :rtype: matplotlib figure

    '''

    for j in range(0, len(model_list)):
        model = model_list[j]
        sol = sol_list[j]
        if model.protocol == 'ivb':
            for i in range(1, model.compartments + 1, 1):
                compartment_name = [
                    'central (qc)',
                    'peripheral 1 (q_p1)',
                    'peripheral 2 (q_p2)'
                ]
                plt.plot(
                    sol.t, sol.y[i - 1, :],
                    label="Model: " + model.name
                    + " Protocol " + model.protocol
                    + " Compartments " + compartment_name[i - 1]
                )
        else:
            for i in range(1, model.compartments + 2, 1):
                compartment_name = [
                    'dose compartment (q0)',
                    'central (qc)',
                    'peripheral 1 (q_p1)',
                    'peripheral 2 (q_p2)'
                ]
                plt.plot(
                    sol.t, sol.y[i - 1, :],
                    label="Model: " + model.name
                    + " Protocol " + model.protocol
                    + " Compartments " + compartment_name[i - 1]
                )

    plt.legend()
    plt.ylabel('Drug Mass [ng]')
    plt.xlabel('Time [hr]')

    plt.show()
