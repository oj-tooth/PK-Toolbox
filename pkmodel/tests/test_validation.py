import pytest


@pytest.mark.parametrize(

    "test, raises",
    [
        (
            'test_model',
            None,
        ),
        (
            '',
            None,
        ),
        (
            3,
            TypeError,
        ),
        (
            ['this', 'is', 'a', 'list'],
            TypeError,
        )
    ])
def test_validate_name(test, raises):
    """Test normalisation works for arrays of one and positive integers."""
    from ..validate import validate_name
    if raises:
        with pytest.raises(raises):
            validate_name(test)


@pytest.mark.parametrize(

    "test, raises",
    [
        (
            'ivb',
            None,
        ),
        (
            'sc',
            None,
        ),
        (
            3,
            ValueError,
        ),
        (
            'hello',
            ValueError,
        )
    ])
def test_validate_protocol(test, raises):
    """Test normalisation works for arrays of one and positive integers."""
    from ..validate import validate_protocol
    if raises:
        with pytest.raises(raises):
            validate_protocol(test)


@pytest.mark.parametrize(

    "test, raises",
    [
        (
            1,
            None,
        ),
        (
            -10,
            ValueError,
        ),
        (
            0,
            ValueError,
        ),
        (
            'test',
            TypeError,
        )
    ])
def test_validate_compartments(test, raises):
    """Test normalisation works for arrays of one and positive integers."""
    from ..validate import validate_compartments
    if raises:
        with pytest.raises(raises):
            validate_compartments(test)


@pytest.mark.parametrize(

    "test, raises",
    [
        (
            {'test': 1},
            None,
        ),
        (
            {'test': 0},
            ValueError,
        ),
        (
            {'test': -10},
            ValueError,
        ),
        (
            {'test': 'string'},
            TypeError,
        )
    ])
def test_validate_params(test, raises):
    """Test normalisation works for arrays of one and positive integers."""
    from ..validate import validate_params
    if raises:
        with pytest.raises(raises):
            validate_params(test)
