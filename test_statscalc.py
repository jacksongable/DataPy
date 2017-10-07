from unittest import TestCase
from StatsCalc import OneVarStatsCalc


class TestOneVariableStatsCalc(TestCase):

    #  Used for testing all of the algorithms
    _oneVarCalcOdd = None

    #  Used in addition to _oneVarCalcOdd when the algorithm of a method changes depending
    #  on whether the data set is of odd or even length (such as the algorithm for solving
    #  the median or quartiles)
    _oneVarCalcEven = None

    def setUp(self):
        _dataOdd = [1, 3, 5, 7, 9, 11, 13]
        _dataEven = [2, 4, 6, 8, 10, 12]

        self._oneVarCalcEven = OneVarStatsCalc(_dataEven)
        self._oneVarCalcOdd = OneVarStatsCalc(_dataOdd)

    def test_mean(self):
        self.assertEqual(7, self._oneVarCalcOdd.mean(), "Mean calculation")

    def test_min(self):
        self.assertEqual(1, self._oneVarCalcOdd.min(), "Minimum calculation")

    def test_max(self):
        self.assertEqual(13, self._oneVarCalcOdd.max(), "Maximum calculation")

    def test_median_odd(self):
        self.assertEqual(7, self._oneVarCalcOdd.median(), "Odd median calculation")

    def test_median_even(self):
        self.assertEqual(7, self._oneVarCalcEven.median(), "Even median calculation")

    def test_q1_odd(self):
        self.assertEqual(3, self._oneVarCalcOdd.q1(), "Odd Q1 calculation")

    def test_q1_even(self):
        self.assertEqual(4, self._oneVarCalcEven.q1(), "Even Q1 calculation")

    def test_q3_odd(self):
        self.assertEqual(11, self._oneVarCalcOdd.q3(), "Odd Q3 calculation")

    def test_q3_even(self):
        self.assertEqual(10, self._oneVarCalcEven.q3(), "Even Q3 calculation")

    def test_range(self):
        self.assertEqual(12, self._oneVarCalcOdd.range(), "Range calculation")

    def test_iqr_odd(self):
        self.assertEqual(8, self._oneVarCalcOdd.iqr(), "Odd IQR calculation")

    def test_iqr_even(self):
        self.assertEqual(6, self._oneVarCalcEven.iqr(), "Even IQR calculation")

    def test_std_dev(self):
        self.assertEqual(4, self._oneVarCalcOdd.std_dev(), "Standard deviation calculation")

    def test_upper_fence(self):
        self.assertEqual(23, self._oneVarCalcOdd.upper_fence(), "Upper fence calculation")

    def test_lower_fence(self):
        self.assertEqual(-9, self._oneVarCalcOdd.lower_fence(), "Lower fence calculation")

    def test_outliers(self):
        outlier_calc = OneVarStatsCalc([0, 50, 51, 52, 53, 999])
        outliers = outlier_calc.outliers()

        for outlier in outliers:
            if outlier != 0 and outlier != 999:
                self.fail("Outlier test failed.")
