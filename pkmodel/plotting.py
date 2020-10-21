import numpy as np 
import matplotlib.pyplot as plt


def plot_singlemodel(model, sol):
    '''
    A function to plot a single model solution

    :param model_list: a model class instance
    :type model_list: model
    :param sol: an object containing sol.t, an array of timesteps; and sol.y, an array of the ODE solutions
    :type sol: object
    :return fig: DESCRIPTION
    :rtype: matplotlib figure

    '''
    fig = plt.figure()

    for i in range(0, model.compartments, 1):
        plt.plot(sol.t, sol.y[i, :], label="Compartments " + i)

    plt.legend()
    plt.ylabel('Drug Mass [ng]')
    plt.xlabel('Time [hr]')

    return fig


def plot_multiplemodels(model_list, sol_list):
    '''
    A function to plot multiple model solutions on the same figure

    :param model_list: A list of model class instances
    :type model_list: list
    :param sol: an list of objects (sol) containing sol.t, an array of timesteps; and sol.y, an array of the ODE solutions
    :type sol: list
    :return fig: DESCRIPTION
    :rtype: matplotlib figure

    '''
    fig = plt.figure()

    for j in range(0, len(model_list)):
        for i in range(0, model_list[j].compartments, 1):
            plt.plot(sol_list[j].t, sol_list[j].y[i, :], label="Model: " + model_list[j].name + " Compartments " + i)

    plt.legend()
    plt.ylabel('Drug Mass [ng]')
    plt.xlabel('Time [hr]')

    return fig
