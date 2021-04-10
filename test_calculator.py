"""
Testing calculator.py
"""

import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtract(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self):
        assert 10 == calculator.multiply(2, 5)
