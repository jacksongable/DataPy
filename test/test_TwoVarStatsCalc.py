#
# Copyright (c) 2017 Jackson Gable
#
# This file is released under the MIT License.
#

from unittest import TestCase
from DataPy import TwoVarStatsCalc


class TestTwoVariableStatsCalc(TestCase):

    def setUp(self):
        x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y_list = [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

        self._var_calc = TwoVarStatsCalc(x_list, y_list)

    def test_init_throws_exception_when_list_lengths_not_equal(self):
        self.assertRaises(Exception, TwoVarStatsCalc, [0, 2], [0])

    def test_r(self):
        expected = 1
        actual = self._var_calc.r()
        fail_msg = "Correlation coefficient algorithm failed. Expected: {}, Actual: {}".format(expected, actual)
        self.assertAlmostEquals(expected, actual, msg=fail_msg)

    def test_r2(self):
        expected = 1
        actual = self._var_calc.r2()
        fail_msg = "Coefficient of determination algorithm failed. Expected: {}, Actual: {}".format(expected, actual)
        self.assertAlmostEquals(expected, actual, msg=fail_msg)

    def test_linear_regression_slope(self):
        expected = 2.0
        actual = self._var_calc.linear_regression_slope()
        fail_msg = "Linear regression slope algorithm failed.\n. Expected:'{}'\nActual: '{}'".format(expected, actual)
        self.assertEquals(expected, actual, msg=fail_msg)

    def test_linear_regression_y_int(self):
        expected = -10.0
        actual = self._var_calc.linear_regression_y_int()
        fail_msg = "Linear regression y-intercept algorithm failed.\n. Expected:'{}'\nActual: '{}'".format(expected, actual)
        self.assertEquals(expected, actual, msg=fail_msg)

    def test_linear_regression_eq(self):
        expected = "y = 2.0x - 10.0"
        actual = self._var_calc.linear_regression_eq()
        fail_msg = "Linear regression equation algorithm failed.\nExpected: '{}'\nActual: '{}'".format(expected, actual)
        self.assertEquals(expected, actual, msg=fail_msg)