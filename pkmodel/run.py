#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:08:39 2020

@author: rebecca
"""

import plotting
import user_inputs
from model import Model
import solve_model

# USER INPUTS

params1 = {
            'Q_p1': 1.0,
            'V_c': 1.0,
            'V_p1': 1.0,
            'CL': 1.0,
            'k_a': 1.5,
            'dose_rate': 2.0,
            't_dose': 3.0,
            't_end': 10.0
        }

params2 = {
            'Q_p1': 2.0,
            'V_c': 13.0,
            'V_p1': 1.0,
            'CL': 1.0,
            'k_a': 1.5,
            'dose_rate': 2.0,
            't_dose': 3.0,
            't_end': 10.0
        }

model_list = [Model('example_name', params1, 1, 'ivb'), Model('example_name2', params2, 2, 'sc')]

# FIND SOLUTIONS
sol_list = []
for model in model_list:
    sol_list.append(solve_model.solve(model))

# PLOT SOLUTIONS
plotting.figure_creator(model_list, sol_list)
