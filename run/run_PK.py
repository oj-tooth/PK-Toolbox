################
# run_PK.py
################

# Import visualisation module.
from pk_toolbox_room8.pkmodel import plotting
# Import Model class module.
from pk_toolbox_room8.pkmodel.model import Model
# Import ODE solver module.
from pk_toolbox_room8.pkmodel import solve_model

# USER INPUT
# Define Example A - 2 Compartment Intravenous Bolus.
name_1 = "Example A"
compartments_1 = 2
protocol_1 = "ivb"
params_1 = {
    'V_c': 1.0,
    'CL': 1.0,
    'k_a': None,
    'dose_rate': 2.0,
    't_dose': 5,
    't_end': 10,
    'Q_p1': 0.5,
    'V_p1': 1.0}

# Define Example B - 2 Compartment Subcutaneous.
name_2 = "Example B"
compartments_2 = 2
protocol_2 = "SC"
params_2 = {
    'V_c': 1.0,
    'CL': 1.0,
    'k_a': 0.5,
    'dose_rate': 2.0,
    't_dose': 5,
    't_end': 10,
    'Q_p1': 0.5,
    'V_p1': 1.0}

# CONFIGUIRE MODELS
model_list = [Model(name_1, params_1, compartments_1, protocol_1),
              Model(name_2, params_2, compartments_2, protocol_2)]

# FIND SOLUTIONS
sol_list = []
for model in model_list:
    sol_list.append(solve_model.solve(model))

# PLOT SOLUTIONS
plotting.figure_creator(model_list, sol_list)
