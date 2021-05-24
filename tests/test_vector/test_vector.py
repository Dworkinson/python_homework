import pytest
from vector.vector import Vector

VECTOR_DEFAULT = 0.0
VECTOR_NEW_VALUE = 2.0


@pytest.mark.parametrize('params', [
    (), (2.0, 3.0)
])
def test_constructor(params):
    vector = Vector(*params)

    assert vector.x == VECTOR_DEFAULT if params == () else params[0]
    assert vector.y == VECTOR_DEFAULT if params == () else params[1]


@pytest.mark.parametrize('x, y, exception_type', [
    ('text', 'text', ValueError), (Vector, Vector, TypeError)
])
def test_constructor_exceptions(x, y, exception_type):
    with pytest.raises(exception_type):
        Vector(x, y)


def test_setters():
    vector = Vector()

    assert vector.x == VECTOR_DEFAULT
    assert vector.y == VECTOR_DEFAULT

    vector.x = VECTOR_NEW_VALUE
    vector.y = VECTOR_NEW_VALUE

    assert vector.x == VECTOR_NEW_VALUE
    assert vector.y == VECTOR_NEW_VALUE


@pytest.mark.parametrize('value, exception_type', [
    ('text', ValueError), (Vector, TypeError)
])
def test_setter_exception(value, exception_type):
    vector = Vector()

    with pytest.raises(exception_type):
        vector.x = value


def test_comparison_operators():
    vector = Vector()
    same_vector = Vector()
    other_vector = Vector(2.0, 3.0)

    assert vector == same_vector
    assert not vector == other_vector
    assert vector != other_vector
    assert not vector != same_vector


def test_comparison_operators_exception():
    vector = Vector()

    with pytest.raises(TypeError):
        vector == "text"


def test_arithmetic_operators():
    vector = Vector()
    other_vector = Vector(2.0, 3.0)

    new_vector = vector + other_vector

    assert new_vector.x == 2.0
    assert new_vector.y == 3.0

    new_vector = vector - other_vector

    assert new_vector.x == -2.0
    assert new_vector.y == -3.0

    new_vector += other_vector

    assert new_vector.x == 0.0
    assert new_vector.y == 0.0

    new_vector -= other_vector

    assert new_vector.x == -2.0
    assert new_vector.y == -3.0


@pytest.mark.parametrize('params, string_repr', [
    ((), '(0.0, 0.0)'), ((2.0, 3.0), '(2.0, 3.0)')
])
def test_string_repr(params, string_repr):
    vector = Vector(*params)

    assert str(vector) == string_repr


def test_length():
    vector = Vector(2.0, 3.0)

    assert vector.length() == 3.6055512754639896
