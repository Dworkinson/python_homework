import pytest
from complex.complex import Complex

COMPLEX_DEFAULT = 0.0


@pytest.mark.parametrize('params', [
    (), (2.0, 3.0)
])
def test_constructor(params):
    complex_number = Complex(*params)

    assert complex_number.real == COMPLEX_DEFAULT if params == () else params[0]
    assert complex_number.imaginary == COMPLEX_DEFAULT if params == () else params[1]


@pytest.mark.parametrize('real, imaginary, exception_type', [
    ('text', 'text', ValueError), (Complex, Complex, TypeError)
])
def test_constructor_exception(real, imaginary, exception_type):
    with pytest.raises(exception_type):
        Complex(real, imaginary)


def test_comparison_operators():
    complex_number = Complex()
    same_complex_number = Complex()
    other_complex_number = Complex(2.0, -3.0)

    assert complex_number == same_complex_number
    assert not complex_number != same_complex_number
    assert complex_number != other_complex_number
    assert not complex_number != same_complex_number


def test_comparison_operators_exception():
    complex_number = Complex()

    with pytest.raises(TypeError):
        complex_number == "text"


def test_arithmetic_operators():
    complex_number = Complex(1.0, 1.0)
    other_complex_number = Complex(2.0, 3.0)

    new_complex_number = complex_number + other_complex_number

    assert new_complex_number.real == 3.0
    assert new_complex_number.imaginary == 4.0

    new_complex_number = complex_number - other_complex_number

    assert new_complex_number.real == -1.0
    assert new_complex_number.imaginary == -2.0

    new_complex_number += other_complex_number

    assert new_complex_number.real == 1.0
    assert new_complex_number.imaginary == 1.0

    new_complex_number -= other_complex_number

    assert new_complex_number.real == -1.0
    assert new_complex_number.imaginary == -2.0

    new_complex_number = complex_number * other_complex_number

    assert new_complex_number.real == -1.0
    assert new_complex_number.imaginary == 5.0

    new_complex_number *= complex_number

    assert new_complex_number.real == -6.0
    assert new_complex_number.imaginary == 4.0

    absolute = abs(new_complex_number)

    assert absolute == 7.211102550927979


@pytest.mark.parametrize('params, string_repr', [
    ((), '0.0+0.0i'), ((2.0, -3.0), '2.0-3.0i')
])
def test_string_repr(params, string_repr):
    complex_number = Complex(*params)

    assert str(complex_number) == string_repr
