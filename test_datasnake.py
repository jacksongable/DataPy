from unittest import TestCase
from DataSnake import OneVarStatsCalc


class TestOneVariableStatsCalc(TestCase):

    def setUp(self):
        odd_length_data = [1, 3, 5, 7, 9, 11, 13]
        even_length_data = [2, 4, 6, 8, 10, 12]
        self.odd_calc = OneVarStatsCalc(odd_length_data)
        self.even_calc = OneVarStatsCalc(even_length_data)

    def test_mean(self):
        self.assertEqual(7, self.odd_calc.mean(), "Mean algorithm failed")
        self.assertEqual(7, self.even_calc.mean(), "Mean algorithm failed")

    def test_min(self):
        self.assertEqual(1, self.odd_calc.min(), "Minimum algorithm failed")
        self.assertEqual(2, self.even_calc.min(), "Minimum algorithm failed")

    def test_max(self):
        self.assertEqual(13, self.odd_calc.max(), "Maximum algorithm failed")
        self.assertEqual(12, self.even_calc.max(), "Maximum algorithm failed")

    def test_median(self):
        self.assertEqual(7, self.odd_calc.median(), "Odd-length median algorithm failed")
        self.assertEqual(7, self.even_calc.median(), "Even-length median algorithm failed")

    def test_q1_odd(self):
        self.assertEqual(3, self.odd_calc.q1(), "Odd-length Q1 algorithm failed")
        self.assertEqual(4, self.even_calc.q1(), "Even-length Q1 algorithm failed")

    def test_q3_odd(self):
        self.assertEqual(11, self.odd_calc.q3(), "Odd-length Q3 calculation")
        self.assertEqual(10, self.even_calc.q3(), "Even-length Q3 calculation")

    def test_range(self):
        self.assertEqual(12, self.odd_calc.range(), "Range algorithm failed")
        self.assertEqual(10, self.even_calc.range(), "Range algorithm failed")

    def test_iqr(self):
        self.assertEqual(8, self.odd_calc.iqr(), "Odd-length IQR algorithm failed")
        self.assertEqual(6, self.even_calc.iqr(), "Even-length IQR algorithm failed")

    def test_std_dev(self):
        self.assertEqual(4, self.odd_calc.std_dev(), "Standard deviation calculation")

    def test_upper_fence(self):
        self.assertEqual(23, self.odd_calc.upper_fence(), "Upper fence algorithm failed")
        self.assertEqual(19, self.even_calc.upper_fence(), "Upper fence algorithm failed")

    def test_lower_fence(self):
        self.assertEqual(-9, self.odd_calc.lower_fence(), "Lower fence algorithm failed")
        self.assertEqual(-5, self.even_calc.lower_fence(), "Lower fence algorithm failed")

    def test_outliers(self):
        outlier_calc = OneVarStatsCalc([0, 50, 51, 52, 53, 999])
        outliers = outlier_calc.outliers()
        for outlier in outliers:
            if outlier != 0 and outlier != 999:
                self.fail("Outlier algorithm failed.")
