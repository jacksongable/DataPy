#
# Copyright (c) 2017 Jackson Gable
#
# This file is released under the MIT License.
#

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

    #  Calculates and returns the mean of the data
    def mean(self, data=None):
        if data is None:
            data = self._data
        total = 0
        for x in data:
            total += x
        return total / len(data)

    #  Calculates and returns the maximum value in the data
    def max(self):
        return self._data[len(self._data) - 1]

    #  Calculates and returns the minimum value in the data
    def min(self):
        return self._data[0]

    #  Calculates and returns the median value in the data
    def median(self, data=None):
        if data is None:  # if method should perform calculation on default data set
            data = self._data

        max_index = len(data) - 1
        if len(data) % 2 == 1:  # odd-length data set
            med_index = max_index // 2
            median = data[med_index]
        else:  # even-length data set, this is where it gets (marginally more) interesting
            lower_med_index = max_index // 2
            upper_med_index = lower_med_index + 1
            median = self.mean([data[lower_med_index], data[upper_med_index]])
        return median

    #  Calculates and returns the first quartile of the data
    def q1(self):
        max_index = len(self._data) - 1
        if len(self._data) % 2 == 1:  # data length is odd
            stop = max_index // 2
        else:  # data length is even
            stop = (max_index // 2) + 1
        return self.median(self._data[0: stop])

    #  Calculates and returns the third quartile of the data
    def q3(self):
        max_index = len(self._data) - 1
        if len(self._data) % 2 == 1:
            start = max_index // 2 + 1
        else:
            start = max_index // 2 + 1
        return self.median(self._data[start: max_index + 1])

    #  Calculates and returns the data's range
    def range(self, data=None):
        if data is None:
            data = self._data
        return data[len(data) - 1] - data[0]

    #  Calculates and returns the data's interquartile range
    def iqr(self):
        return self.q3() - self.q1()

    #  Calculates and returns the population standard deviation of the data
    def pop_std_dev(self):
        count_inverse = len(self._data) ** -1
        squared_variance_sum = 0
        mean = self.mean()  # Prevents self.mean() from running during each for loop iteration
        for val in self._data:
            squared_variance_sum += (val - mean) ** 2

        std_dev_square = count_inverse * squared_variance_sum
        return sqrt(std_dev_square)

    #  Calculates and returns the sample standard deviation of the data
    #  TODO: Write test method for this
    def std_dev(self):
        count_inverse = (len(self._data) - 1) ** -1
        squared_variance_sum = 0
        mean = self.mean()  # Prevents self.mean() from running during each for loop iteration
        for val in self._data:
            squared_variance_sum += (val - mean) ** 2

        std_dev_square = count_inverse * squared_variance_sum
        return sqrt(std_dev_square)

    #  Calculates and returns the upper fence of the data.
    #  Numbers in the data set higher than the value of the upper fence are considered outliers
    def upper_fence(self):
        return self.iqr() * 1.5 + self.q3()

    #  Calculates and returns the lower fence of the data.
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


#  This class accepts two lists of equal length, the first being the list of x-values
#  and the second being the list of y-values.

class TwoVarStatsCalc:

    def __init__(self, x_list, y_list):
        if len(x_list) == len(y_list):
            self._x_list = x_list
            self._y_list = y_list
            self._x_calc = OneVarStatsCalc(x_list)
            self._y_calc = OneVarStatsCalc(y_list)

            # This variable is also equal to len(self._y_list), since len(self._x_list) == len(self._y_list)
            self._data_length = len(self._x_list)
        else:
            raise Exception("Lists must be of equal length.")

    # Calculates and returns the correlation coefficient of the data
    def r(self):
        x_mean = self._x_calc.mean()
        y_mean = self._y_calc.mean()

        x_sd = self._x_calc.std_dev()
        y_sd = self._y_calc.std_dev()

        x_z_scores = []
        y_z_scores = []

        for x in self._x_list:
            z = (x - x_mean) / x_sd
            x_z_scores.append(z)
        for y in self._y_list:
            z = (y - y_mean) / y_sd
            y_z_scores.append(z)

        z_products = []
        for index in range(0, self._data_length):
            z = x_z_scores[index] * y_z_scores[index]
            z_products.append(z)
        z_sum = 0
        for z in z_products:
            z_sum += z

        return z_sum / (self._data_length - 1)

    #  Calculates the coefficient of determination of the data
    def r2(self):
        return self.r() ** 2

    #  Calculates and returns the slope of the linear regression line
    def linear_regression_slope(self):
        return self.r() * self._y_calc.std_dev() / self._x_calc.std_dev()

    #  Calculates and returns the y-intercept of the linear regression line
    def linear_regression_y_int(self):
        return self._y_calc.mean() - self.linear_regression_slope() * self._x_calc.mean()

    #  Calculates the equation of the linear regression line and returns it as a string
    def linear_regression_eq(self):
        m = self.linear_regression_slope()
        b = self.linear_regression_y_int()
        if b < 0:
            return "y = {}x - {}".format(m, fabs(b))
        elif b > 0:
            return "y = {}x + {}".format(m, b)
        elif b == 0: # Very unlikely, just covering all the bases.
            return "y = {}x".format(m)


