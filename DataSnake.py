from __future__ import division
from math import sqrt
from math import fabs

#
# This class performs 1-variable statistics calculations on the data set it is initialized with.
#


class OneVarStatsCalc:

    def __init__(self, data):
        data.sort()
        self._data = data

    #  Calculates the mean of the data
    def mean(self, data=None):
        if data is None:
            data = self._data
        total = 0
        for x in data:
            total += x
        return total / len(data)

    #  Calculates the maximum value in the data
    def max(self):
        return self._data[len(self._data) - 1]

    #  Calculates the minimum value in the data
    def min(self):
        return self._data[0]

    #  Calculates the median value in the data
    def median(self, data=None):
        if data is None:  # if method should perform calculation on default data set
            data = self._data

        max_index = len(data) - 1
        if len(data) % 2 == 1:  # odd-length data set
            med_index = max_index / 2
            median = data[med_index]
        else:  # even-length data set, this is where it gets (marginally more) interesting
            lower_med_index = max_index // 2
            upper_med_index = lower_med_index + 1
            median = self.mean([data[lower_med_index], data[upper_med_index]])
        return median

    #  Calculates the first quartile of the data
    def q1(self):
        max_index = len(self._data) - 1
        if len(self._data) % 2 == 1:  # data length is odd
            stop = max_index / 2
        else:  # data length is even
            stop = (max_index // 2) + 1
        return self.median(self._data[0: stop])

    #  Calculates the third quartile of the data
    def q3(self):
        max_index = len(self._data) - 1
        if len(self._data) % 2 == 1:
            start = max_index / 2 + 1
        else:
            start = max_index // 2 + 1
        return self.median(self._data[start: max_index + 1])

    #  Calculates the data's range
    def range(self, data=None):
        if data is None:
            data = self._data
        return data[len(data) - 1] - data[0]

    #  Calculates the data's interquartile range
    def iqr(self):
        return self.q3() - self.q1()

    #  Calculates the population standard deviation of the data
    def pop_std_dev(self):
        count_inverse = len(self._data) ** -1
        squared_variance_sum = 0
        mean = self.mean()  # Prevents self.mean() from running during each for loop iteration
        for val in self._data:
            squared_variance_sum += (val - mean) ** 2

        std_dev_square = count_inverse * squared_variance_sum
        return sqrt(std_dev_square)

    def std_dev(self):
        count_inverse = (len(self._data) - 1) ** -1
        squared_variance_sum = 0
        mean = self.mean()  # Prevents self.mean() from running during each for loop iteration
        for val in self._data:
            squared_variance_sum += (val - mean) ** 2

        std_dev_square = count_inverse * squared_variance_sum
        return sqrt(std_dev_square)

    #  Calculates the upper fence of the data.
    #  Numbers in the data set higher than the value of the upper fence are considered outliers
    def upper_fence(self):
        return self.iqr() * 1.5 + self.q3()

    #  Calculates the lower fence of the data.
    #  Numbers in the data set lower than the value of the lower fence are considered outliers
    def lower_fence(self):
        return self.q1() - self.iqr() * 1.5

    #  Calculates and returns the outliers in the data set
    def outliers(self):
        outliers = []
        uf = self.upper_fence()
        lf = self.lower_fence()
        for x in self._data:
            if x > uf or x < lf:
                outliers.append(x)
        return outliers


class TwoVarStatsCalc:

    def __init__(self, x_list, y_list):
        if len(x_list) == len(y_list):
            self._x_list = x_list
            self._y_list = y_list
        else:
            raise Exception("Lists must be of equal length.")

    # Calculates the correlation coefficient of the data
    def r(self):
        x_calc = OneVarStatsCalc(self._x_list)
        y_calc = OneVarStatsCalc(self._y_list)

        x_mean = x_calc.mean()
        y_mean = y_calc.mean()

        x_sd = x_calc.std_dev()
        y_sd = y_calc.std_dev()

        x_z_scores = []
        y_z_scores = []

        for x in self._x_list:
            z = (x - x_mean) / x_sd
            x_z_scores.append(z)
        for y in self._y_list:
            z = (y - y_mean) / y_sd
            y_z_scores.append(z)

        z_products = []
        for index in range(0, (len(self._x_list))):
            z = x_z_scores[index] * y_z_scores[index]
            z_products.append(z)
        z_sum = 0
        for z in z_products:
            z_sum += z

        return z_sum / (len(self._x_list) - 1)

    #  Calculates the coefficient of determination of the data
    def r2(self):
        return self.r() ** 2

    #  Calculates the equation of the linear regression line
    def lin_reg_eq(self):
        x_calc = OneVarStatsCalc(self._x_list)
        y_calc = OneVarStatsCalc(self._y_list)

        m = self.r() * y_calc.std_dev() / x_calc.std_dev()
        b = y_calc.mean() - m * x_calc.mean()

        if b < 0:
            return "y = {}x - {}".format(m, fabs(b))
        else:
            return "y = {}x + {}".format(m, b)
