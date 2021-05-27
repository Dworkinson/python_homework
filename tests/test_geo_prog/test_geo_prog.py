import pytest

from geo_prog.geo_prog import geo_prog


def test_ageo_prog():
    test_generator = geo_prog(1, 10, 2)
    expected_results = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    for result in expected_results:
        assert next(test_generator) == result

    with pytest.raises(StopIteration):
        next(test_generator)
