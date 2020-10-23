from ..model import Model
import pytest
import numpy

model_sc = Model('test_model',
                 params={
                     'Q_p1': 1.0,
                     'V_c': 1.0,
                     'V_p1': 1.0,
                     'CL': 1.0,
                     'k_a': 1.5,
                     'dose_rate': 2.0,
                     't_end': 10.0,
                     't_dose': 3
                     },  # noqa:E123
                 compartments=1,
                 protocol='sc'
                 )

model_ivb = Model('test_model',
                  params={
                      'Q_p1': 1.0,
                      'V_c': 1.0,
                      'V_p1': 1.0,
                      'CL': 1.0,
                      'k_a': 1.5,
                      'dose_rate': 2.0,
                      't_end': 10.0,
                      't_dose': 3
                      },  # noqa:E123
                  compartments=1,
                  protocol='ivb'
                  )


@pytest.mark.parametrize(
    "test, expected, raises",
    [
        (
            [2, 2, 5], 2, None
        ),
        (
            [0, 0, 0], 0, None
        ),
        (
            [0, 5, 0], 5, None
        )
    ])
def test_dose(test, expected, raises):
    """Tests dose function from solve_model returns correct
    heaviside step function values.
    """
    from .. import solve_model
    assert solve_model.dose(*test) == expected


@pytest.mark.parametrize(
    "test, expected, raises",
    [
        (
            model_ivb, numpy.array([0.0, 0.0]), None
        ),
        (
            model_sc, numpy.array([0.0, 0.0, 0.0]), None
        )
    ])
def test_initial_conditions(test, expected, raises):
    """Tests dose function from solve_model returns correct
    heaviside step function values.
    """
    from .. import solve_model
    assert numpy.array_equal(solve_model.initial_conditions(test), expected)


@pytest.mark.parametrize(
    "test, expected, raises",
    [
        (
            model_sc, True, None
        ),
        (
            model_ivb, True, None
        )
    ])
def test_solve_type(test, expected, raises):
    """Tests that solution outputted by solve_model.solve() function
    is a numpy ndarray.

    :param model_init: pytest fixture function which generates an instance
        of Model class.
    """
    from .. import solve_model
    assert isinstance(solve_model.solve(test).y, numpy.ndarray)


@pytest.mark.parametrize(
    "test, expected, raises",
    [
        (
            model_sc, True, None
        ),
        (
            model_ivb, True, None
        )
    ])
def test_solve_shape(test, expected, raises):
    """Tests that solution's time array is same length as concentration array.

    :param model_init: pytest fixture function which generates an instance
        of Model class.
    """
    from .. import solve_model
    assert solve_model.solve(test).y.shape[1] == solve_model.solve(test).t.shape[0]
