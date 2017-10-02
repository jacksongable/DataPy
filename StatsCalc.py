#
# This class performs 1-variable statistics calculations on the data set it is initialized with.
#


class OneVariableStatsCalc:
    _data = []

    def __init__(self, data):
        data.sort()
        self._data = data

    def mean(self, data=None):
        if data is None:
            data = self._data
        total = 0
        for x in data:
            total += x
        return total / len(data)

    def max(self):
        current_max = self._data[0]
        for element in self._data:
            if element > current_max:
                current_max = element
        return current_max

    def min(self):
        current_min = self._data[0]
        for element in self._data:
            if element < current_min:
                current_min = element
        return current_min

    def median(self, data=None):
        if data is None:  # if method should perform calculation on default data set
            data = self._data

        max_index = len(data) - 1
        if len(data) % 2 == 1:  # odd-length data set algorithm
            med_index = max_index / 2
            median = data[med_index]
        else:  # even-length data set algorithm, this is where it gets (marginally more) interesting
            lower_med_index = max_index // 2
            upper_med_index = lower_med_index + 1
            median = self.mean([data[lower_med_index], data[upper_med_index]])
        return median

    def q1(self):
        max_index = len(self._data) - 1
        if len(self._data) % 2 == 1:  # data length is odd
            stop = max_index / 2
        else:  # data length is even
            stop = (max_index // 2) + 1
        return self.median(self._data[0: stop])

    def q3(self):
        max_index = len(self._data) - 1
        if len(self._data) % 2 == 1:
            start = max_index / 2 + 1
        else:
            start = max_index // 2 + 1
        return self.median(self._data[start : len(self._data)])

    def range(self, data=None):
        if data is None:
            data = self._data
        return data[len(data) - 1] - data[0]

    def iqr(self):
        return self.q3() - self.q1()
