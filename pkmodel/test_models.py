from model import Model
import pytest
import numpy

@pytest.fixture
def model_init():
    params = {
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'k_a': 1.5,
    'dose_rate': 2.0,
    't_end': 10.0,
    't_dose': 3
    }
    return Model('test_model', params, compartments=1) 

@pytest.fixture
def model_init_2comp():
    params = {
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'k_a': 1.5,
    'dose_rate': 2.0,
    't_end': 10.0,
    't_dose': 3
    }
    return Model('test_model', params, compartments=2) 


def test_solve_output_type(model_init):
    
    import solve_model
    assert isinstance(solve_model.solve(model_init).y, numpy.ndarray)


def test_solve_output_shape(model_init):
    
    import solve_model
    assert solve_model.solve(model_init).y.shape[0,:] == solve_model.solve(model_init).t.shape[0,:]