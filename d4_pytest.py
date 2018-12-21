import pytest
import d3_common


class TestD3Common(object):
    def test_factorial(self):
        assert d3_common.factorial(2) == 2

