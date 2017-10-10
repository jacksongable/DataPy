from unittest import TestCase
from DataSnake import  TwoVarStatsCalc


class TestTwoVariableStatsCalc(TestCase):

    def setUp(self):
        x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y_list = [-8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

        self._var_calc = TwoVarStatsCalc(x_list, y_list)

    def test_init_throws_exception_when_list_lengths_not_equal(self):
        self.assertRaises(Exception, TwoVarStatsCalc, [0, 2], [0])

    def test_r(self):
        fail_msg = "Correlation coefficient algorithm failed. Expected: {}, Actual: {}".format(1, self._var_calc.r())
        self.assertAlmostEquals(1, self._var_calc.r(), msg=fail_msg)

    def test_r2(self):
        fail_msg = "Coefficient of determination algorithm failed. Expected: {}, Actual: {}".format(1, self._var_calc.r2())
        self.assertAlmostEquals(1, self._var_calc.r2(), msg=fail_msg)

    def test_lin_reg_eq(self):
        expected = "y = 2.0x - 10.0"
        actual = self._var_calc.lin_reg_eq()
        fail_msg = "Linear regression algorithm failed.\nExpected: '{}'\nActual: '{}'".format(expected, actual)
        self.assertEquals(expected, actual, msg=fail_msg)