#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:08:39 2020

@author: rebecca
"""
# Import visualisation module.
import plotting 
# Import Model class module.
from model import Model
# Import ODE solver module.
import solve_model
# Import tkinter package.
from tkinter import *

# USER INPUT 

# Configuire empty list model_list.
model_list = []

def config_model():
    """Configures PK model.

    Extracts variables from GUI to create named Model class member.
    
    Finish Docstrings!!!
    """
    name = str(name_entry.get())

    compartments = int(comp_entry.get()) 

    protocol = str(protocol_entry.get())
    
    try:
        if compartments = 1:
            Q_p1 = None
            V_p1 = None
        else:
            Q_p1 = float(Qp1_entry.get())
            V_p1 = float(Vp1_entry.get())

        params = {
                'V_c': float(Vc_entry.get()),
                'CL': float(CL_entry.get()),
                'k_a': float(ka_entry.get()),
                'dose_rate': float(Dose_entry.get()),
                't_dose': float(tdose_entry.get()),
                't_end': float(tend_entry.get()),
                'Q_p1': Q_p1,
                'V_p1': V_p1
            }
    except TypeError: 
        print("TypeError: All parameters should be floating point numbers (e.g. 1.0).")

    model_list.append(Model(name, params, compartments, protocol.lower()))

    summary_label = Label(my_window, text = "Configured: " + name)
    summary_label.grid(row = 4, column = 5)

# Define GUI window, my_window.
my_window =Tk()
# Give window toolbar title.
my_window.title("PK Toolbox Models")

# Add title label to top of window.
Title_label = Label(my_window, text = "PK Toolbox Console", bg = "white smoke", font=("Verdana 22 bold"))
Title_label.grid(row = 0, column = 0)
# Add PK Toolbox logo.
logo = PhotoImage("images/Logo_Image.png")
Logo_label = Label(my_window, image = logo)
Logo_label.grid(row = 0, column = 2)

# User input for model name.
name_label = Label(my_window, text = "Model Name:", font=("Verdana 15 bold"))
name_label.grid(row = 1, column = 0)
name_entry = Entry(my_window)
name_entry.grid(row = 1, column= 1)

# User input for compartment no.
comp_label = Label(my_window, text = "No. Compartments [0/1/2]:", font=("Verdana 15 bold"))
comp_label.grid(row = 1, column = 2)
comp_entry = Entry(my_window)
comp_entry.grid(row = 1, column= 3)

# User input for the dosing protocol.
protocol_label = Label(my_window, text = "Dosing Protocol [IVB/SC]:", font=("Verdana 15 bold"))
protocol_label.grid(row = 1, column = 4)
protocol_entry = Entry(my_window)
protocol_entry.grid(row = 1, column= 5)

# Add Parameter title.
Parameter_label = Label(my_window, text = "Parameters:", font=("Verdana 16 bold"))
Parameter_label.grid(row = 2, column = 0)

# User input for all PK model parameters.
Dose_label = Label(my_window, text = "Dose(t) [ng/hr]:")
Dose_label.grid(row = 3, column = 0)
Dose_entry = Entry(my_window)
Dose_entry.grid(row = 4,column= 0)

Vc_label = Label(my_window, text = "Vc [mL]:")
Vc_label.grid(row = 5, column = 0)
Vc_entry = Entry(my_window)
Vc_entry.grid(row = 6,column= 0)

Vp1_label = Label(my_window, text = "Vp1 [mL]:")
Vp1_label.grid(row = 3, column = 1)
Vp1_entry = Entry(my_window)
Vp1_entry.grid(row= 4,column= 1)

Qp1_label = Label(my_window, text = "Qp1 [mL]:")
Qp1_label.grid(row = 5, column = 1)
Qp1_entry = Entry(my_window)
Qp1_entry.grid(row= 6,column= 1)

ka_label = Label(my_window, text = "ka [/hr]:")
ka_label.grid(row = 3, column = 2)
ka_entry = Entry(my_window)
ka_entry.grid(row= 4,column= 2)

CL_label = Label(my_window, text = "CL [mL/hr]:")
CL_label.grid(row = 3, column = 3)
CL_entry = Entry(my_window)
CL_entry.grid(row= 4,column= 3)

tdose_label = Label(my_window, text = "t_dose [hr]:")
tdose_label.grid(row = 3, column = 4)
tdose_entry = Entry(my_window)
tdose_entry.grid(row = 4,column = 4)

tend_label = Label(my_window, text = "t_end [hr]:")
tend_label.grid(row = 5, column = 4)
tend_entry = Entry(my_window)
tend_entry.grid(row = 6,column = 4)

# Add button for users to add PK model configs.
button = Button(my_window, text = "Add PK Model", font=("Verdana 14"), command = config_model)
button.grid(row = 5,column = 5)
# Add button to end configuration - This could trigger running the simulations.
button = Button(my_window, text = "Run Models", font=("Verdana 14"), command = my_window.quit)
button.grid(row = 6,column = 5)

# End window loop.
my_window.mainloop()



# FIND SOLUTIONS
sol_list = []
for model in model_list:
    sol_list.append(solve_model.solve(model))

# PLOT SOLUTIONS
plotting.figure_creator(model_list, sol_list)
