from unittest import TestCase
from StatsCalc import OneVariableStatsCalc


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

        self._oneVarCalcEven = OneVariableStatsCalc(_dataEven)
        self._oneVarCalcOdd = OneVariableStatsCalc(_dataOdd)

    def test_mean(self):
        self.assertEqual(7, self._oneVarCalcOdd.mean(), "Odd mean calculation")

    def test_min(self):
        self.assertEqual(1, self._oneVarCalcOdd.min(), "Odd minimum calculation")

    def test_max(self):
        self.assertEqual(13, self._oneVarCalcOdd.max(), "Odd maximum calculation")

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
        self.assertEqual(12, self._oneVarCalcOdd.range(), "Odd range calculation")

    def test_iqr_odd(self):
        self.assertEqual(8, self._oneVarCalcOdd.iqr(), "Odd IQR calculation")

    def test_iqr_even(self):
        self.assertEqual(6, self._oneVarCalcEven.iqr(), "Even IQR calculation")

    def test_std_dev(self):
        self.assertEqual(4, self._oneVarCalcOdd.std_dev(), "Standard deviation calculation")