import solve_model
from model import Model
"""This script initialises the model and solves it to produce
the sol object.

if protocol = 0 (IVB)
sol.t is a list of the timesteps of length N
sol.y is a (2,N) numpy array containing the concentrations:
q_c in sol.y[0,:]
q_p1 in sol.y[1,:]

if protocol = 1 (subcutaneous)
sol.t is a list of the timesteps of length N
sol.y is a (3,N) numpy array containing the concentrations:
q_0 in sol.y[0,:]
q_c in sol.y[1,:]
q_p1 in sol.y[2,:]
"""

#initialise the model we want to solve
model=Model('model1',compartments=1,protocol=1)

#I think compartments needs to come in the user input as this is equivalent
#to setting Q_p1=0 or not in model.params

sol = solve_model.solve(model)
