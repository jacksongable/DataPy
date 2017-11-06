#
# Copyright (c) 2017 Jackson Gable
#
# This file is released under the MIT License.
#

from unittest import TestCase
from DataPy import OneVarStatsCalc


class TestOneVariableStatsCalc(TestCase):

    def setUp(self):
        odd_length_int_data = [1, 3, 5, 7, 9, 11, 13]
        even_length_int_data = [2, 4, 6, 8, 10, 12]

        odd_length_float_data = [1.1, 2.4, 6.4, 7.8, 9.02, 10.336, 12.572]
        even_length_float_data = [0.53, 1.5, 4.5, 2.33, 8.5, 13.89]

        self.odd_int_calc = OneVarStatsCalc(odd_length_int_data)
        self.even_int_calc = OneVarStatsCalc(even_length_int_data)

        self.odd_float_calc = OneVarStatsCalc(odd_length_float_data)
        self.even_float_calc = OneVarStatsCalc(even_length_float_data)

    def test_mean(self):
        self.assertEqual(7, self.odd_int_calc.mean(), "Mean algorithm failed for odd-length int data")
        self.assertEqual(7, self.even_int_calc.mean(), "Mean algorithm failed for even-length int data")
        self.assertAlmostEquals(7.08971428571, self.odd_float_calc.mean(), msg="Mean algorithm failed for odd-length "
                                                                               "float data")
        self.assertAlmostEquals(5.20833333, self.even_float_calc.mean(), msg="Mean algorithm failed for even-length float data")

    def test_min(self):
        self.assertEqual(1, self.odd_int_calc.min(), "Minimum algorithm failed for odd-length int data")
        self.assertEqual(2, self.even_int_calc.min(), "Minimum algorithm failed for even-length int data")
        self.assertAlmostEquals(1.1, self.odd_float_calc.min(), msg="Mean algorithm failed for odd-length float data")
        self.assertAlmostEquals(0.53, self.even_float_calc.min(), msg="Mean algorithm failed for even-length float data")

    def test_max(self):
        self.assertEqual(13, self.odd_int_calc.max(), "Maximum algorithm failed for odd-length int data")
        self.assertEqual(12, self.even_int_calc.max(), "Maximum algorithm failed for even-length int data")
        self.assertAlmostEquals(12.572, self.odd_float_calc.max(), "Maximum algorithm failed for odd-length float data")
        self.assertAlmostEquals(13.89, self.even_float_calc.max(), "Maximum algorithm failed for even-length float data")

    def test_median(self):
        self.assertEqual(7, self.odd_int_calc.median(), "Median algorithm failed for odd-length int data")
        self.assertEqual(7, self.even_int_calc.median(), "Median algorithm failed for even-length int data")
        self.assertAlmostEquals(7.8, self.odd_float_calc.median(), msg="Median algorithm failed for odd-length float data")
        self.assertAlmostEquals(3.415, self.even_float_calc.median(), msg="Median algorithm failed for even-length float data")

    def test_q1(self):
        self.assertEqual(3, self.odd_int_calc.q1(), "Q1 algorithm failed for odd-length int data")
        self.assertEqual(4, self.even_int_calc.q1(), "Q1 algorithm failed for even-length int data")
        self.assertAlmostEquals(2.4, self.odd_float_calc.q1(), msg="Q1 algorithm failed for odd-length float data")
        self.assertAlmostEquals(1.5, self.even_float_calc.q1(), msg="Q1 algorithm failed for even-length float data")

    def test_q3(self):
        self.assertEqual(11, self.odd_int_calc.q3(), "Q3 algorithm failed for odd-length int data")
        self.assertEqual(10, self.even_int_calc.q3(), "Q3 algorithm failed for even-length int data")
        self.assertAlmostEquals(10.336, self.odd_float_calc.q3(), msg="Q3 algorithm failed for odd-length float data")
        self.assertAlmostEquals(8.5, self.even_float_calc.q3(), msg="Q3 algorithm failed for even-length float data")

    def test_range(self):
        self.assertEqual(12, self.odd_int_calc.range(), "Range algorithm failed for odd-length int data")
        self.assertEqual(10, self.even_int_calc.range(), "Range algorithm failed for even-length int data")
        self.assertAlmostEquals(11.472, self.odd_float_calc.range(), msg="Range algorithm failed for odd-length float data")
        self.assertAlmostEquals(13.36, self.even_float_calc.range(), msg="Range algorithm failed for even-length float data")

    def test_iqr(self):
        self.assertEqual(8, self.odd_int_calc.iqr(), "Odd-length IQR algorithm failed")
        self.assertEqual(6, self.even_int_calc.iqr(), "Even-length IQR algorithm failed")
        self.assertAlmostEquals(7.936, self.odd_float_calc.iqr(), "IQR algorithm failed for odd-length float data")
        self.assertAlmostEquals(7.0, self.even_float_calc.iqr(), "IQR algorithm failed for even-length float data")

    def test_pop_std_dev(self):
        self.assertEqual(4, self.odd_int_calc.pop_std_dev(), "Standard deviation algorithm failed for odd-length int data")
        self.assertAlmostEquals(3.41565025, self.even_int_calc.pop_std_dev(), msg="Standard deviation algorithm failed for even-length int data")
        self.assertAlmostEquals(3.8390873, self.odd_float_calc.pop_std_dev(), msg="Standard deviation algorithm failed for odd-length float data")
        self.assertAlmostEquals(4.66603835, self.even_float_calc.pop_std_dev(), msg="Standard deviation algorithm failed for even-length float data")

    def test_upper_fence(self):
        self.assertEqual(23, self.odd_int_calc.upper_fence(), "Upper fence algorithm failed for odd-length int data")
        self.assertEqual(19, self.even_int_calc.upper_fence(), "Upper fence algorithm failed for even-length float data")
        self.assertAlmostEquals(22.24, self.odd_float_calc.upper_fence(), msg="Upper fence algorithm failed for odd-length float data")
        self.assertAlmostEquals(19.0, self.even_float_calc.upper_fence(), msg="Upper fence algorithm failed for even-length float data")

    def test_lower_fence(self):
        self.assertEqual(-9, self.odd_int_calc.lower_fence(), "Lower fence algorithm failed for odd-length int data")
        self.assertEqual(-5, self.even_int_calc.lower_fence(), "Lower fence algorithm failed for even-length int data")
        self.assertAlmostEquals(-9.504, self.odd_float_calc.lower_fence(), msg="Lower fence algorithm failed for odd-length float data")
        self.assertAlmostEquals(-9.0, self.even_float_calc.lower_fence(), msg="Lower fence algorithm failed for even-length float data")

    def test_outliers(self):
        outlier_calc = OneVarStatsCalc([0, 50, 51, 52, 53, 999])
        outliers = outlier_calc.outliers()
        for outlier in outliers:
            if outlier != 0 and outlier != 999:
                self.fail("Outlier algorithm failed.")
