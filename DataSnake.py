from math import sqrt

#
# This class performs 1-variable statistics calculations on the data set it is initialized with.
#


class OneVarStatsCalc:

    __data = None

    def __init__(self, data):
        data.sort()
        self.__data = data

    #  Calculates the mean of the data
    def mean(self, data=None):
        if data is None:
            data = self.__data
        total = 0
        for x in data:
            total += x
        return total / len(data)

    #  Calculates the maximum value in the data
    def max(self):
        return self.__data[len(self.__data) - 1]

    #  Calculates the minimum value in the data
    def min(self):
        return self.__data[0]

    #  Calculates the median value in the data
    def median(self, data=None):
        if data is None:  # if method should perform calculation on default data set
            data = self.__data

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
        max_index = len(self.__data) - 1
        if len(self.__data) % 2 == 1:  # data length is odd
            stop = max_index / 2
        else:  # data length is even
            stop = (max_index // 2) + 1
        return self.median(self.__data[0: stop])

    #  Calculates the third quartile of the data
    def q3(self):
        max_index = len(self.__data) - 1
        if len(self.__data) % 2 == 1:
            start = max_index / 2 + 1
        else:
            start = max_index // 2 + 1
        return self.median(self.__data[start: max_index + 1])

    #  Calculates the data's range
    def range(self, data=None):
        if data is None:
            data = self.__data
        return data[len(data) - 1] - data[0]

    #  Calculates the data's interquartile range
    def iqr(self):
        return self.q3() - self.q1()

    #  Calculates the population standard deviation of the data
    def std_dev(self):
        count_inverse = len(self.__data) ** -1
        squared_variance_sum = 0
        mean = self.mean() #  Prevents self.mean() from running during each for loop iteration
        for val in self.__data:
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
        for x in self.__data:
            if x > uf or x < lf:
                outliers.append(x)
        return outliers


class TwoVarStatsCalc:

    __x_list = None
    __y_list = None
    __data_length = None

    def __init__(self, x_list, y_list):
        if len(x_list) != len(y_list):
            raise Exception("Lists of x-values and y-values must be of equal length.")
        else:
            self.__x_list = x_list
            self.__y_list = y_list
            self.__data_length = len(self.__x_list) #  Lengths of self.__x_list and self.__y_list are equal

    def r(self):
        x_calc = OneVarStatsCalc(self.__x_list)
        y_calc = OneVarStatsCalc(self.__y_list)

        x_mean = x_calc.mean()
        y_mean = y_calc.mean()

        sd_x = x_calc.std_dev()
        sd_y = y_calc.std_dev()

        z_scores_x = []
        for x in self.__x_list:
            z_scores_x.append((x - x_mean) / sd_x)
        z_scores_y = []
        for y in self.__y_list:
            z_scores_y.append((y - y_mean) / sd_y)

        z_prod = []
        for index in range(len(z_scores_x)):
            z_prod.append(z_scores_x[index] * z_scores_y[index])

        z_sum = 0
        for val in z_prod:
            z_sum += val

        return z_sum / (self.__data_length - 1)

    def r2(self):
        return self.r() ** 2
