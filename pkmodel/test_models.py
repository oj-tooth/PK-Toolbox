from model import Model
import pytest


@pytest.fixture
def model_init():
    params = {
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'k_a': 1.5,
    'dose_rate': 2.0,
    't_end': 10.0
    }
    return Model('test_model', params, compartments=1) 
def test_solve(model_init):
    
    
    import solve_model
    print(solve_model.solve(model_init))
        

    


"""
def test_rhs(test, expected, raises):
    
    from solve_model import rhs

    #if raises:
    #    with pytest.raises(raises):
    #        # Wait until I have an actual error to raise here
    #else:
    assert expected == rhs(test)
"""