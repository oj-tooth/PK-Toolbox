import matplotlib.pyplot as plt


def figure_creator(model_list, sol_list):
    '''

    :param model_list: A list of model class instances
    :type model_list: list
    :param sol: an list of objects (sol) containing sol.t, an array of timesteps; and sol.y, an array of the ODE solutions
    :type sol: list
    :return fig: visualisation of solutions to model(s)
    :rtype: matplotlib figure

    '''

    for j in range(0, len(model_list)):
        model = model_list[j]
        sol = sol_list[j]
        for i in range(0, model.compartments, 1):
            plt.plot(sol.t, sol.y[i, :], label="Model: " + model.name + " Compartments " + i)
    plt.legend()
    plt.ylabel('Drug Mass [ng]')
    plt.xlabel('Time [hr]')

    plt.show()
