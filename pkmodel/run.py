#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:08:39 2020

@author: rebecca
"""

import plotting
import user_inputs
# USER INPUTS
model_list = user_inputs.user_inputs()

# FIND SOLUTIONS
sol_list = []
for model in model_list:
    sol_list.append(SOLUTIONFUNCTION(model))

# PLOT SOLUTIONS
plotting.figure_creator(model_list, sol_list)
