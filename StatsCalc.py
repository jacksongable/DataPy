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
        current_max = self.__data[0]
        for element in self.__data:
            if element > current_max:
                current_max = element
        return current_max

    #  Calculates the minimum value in the data
    def min(self):
        current_min = self.__data[0]
        for element in self.__data:
            if element < current_min:
                current_min = element
        return current_min

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