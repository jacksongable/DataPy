#
# This class performs 1-variable statistics calculations on the data set it is initialized with.
# Since the data set is immutable, each bound method only runs the necessary calculations once
# in order to increase efficiency.
#


class OneVariableStatsCalc:
    _data = []
    _mean = None
    _max = None
    _min = None
    _med = None
    _q1 = None
    _q3 = None
    _range = None
    _iqr = None

    def __init__(self, data):
        data.sort()
        self._data = data

    def mean(self, data=None):
        if data is None and self._mean is not None:
            return self._mean
        if data is None:
            data = self._data
        total = 0
        for x in data:
            total += x
        mean = total / len(data)
        if data is None and self._mean is None:
            self._mean = mean
        return mean

    def max(self):
        if self._max is not None:
            return self._max
        current_max = self._data[0]
        for element in self._data:
            if element > current_max:
                current_max = element
        self._max = current_max
        return self._max

    def min(self):
        if self._min is not None:
            return self._min
        current_min = self._data[0]
        for element in self._data:
            if element < current_min:
                current_min = element
        self._min = current_min
        return self._min

    def median(self, data=None):
        if data is None and self._med is not None:  # if method has already performed calculation on default data set
            return self._med

        if data is None:  # if method has not already executed and should perform calculation on default data set
            data = self._data

        max_index = len(data) - 1

        if len(data) % 2 == 1:  # odd-length data set algorithm
            med_index = max_index / 2
            self._med = data[med_index]

        else:  # even-length data set algorithm, this is where it gets (marginally more) interesting
            lower_med_index = max_index // 2
            upper_med_index = lower_med_index + 1
            self._med = self.mean([data[lower_med_index], data[upper_med_index]])
        return self._med

    def q1(self):
        if self._q1 is not None:  # if calculation has already been performed
            return self._q1

        max_index = len(self._data) - 1
        if len(self._data) % 2 == 1:  # data length is odd
            stop = max_index / 2
        else:  # data length is even
            stop = (max_index // 2) + 1
        self._q1 = self.median(self._data[0: stop])
        return self._q1

    def q3(self):
        if self._q3 is not None:
            return self._q3
        if len(self._data) % 2 == 1:
            start = (len(self._data) // 2) + 1
        else:
            start = len(self._data) / 2
        self._q3 = self.median(self._data[start : len(self._data)])
        return self._q3

    def range(self, data=None):
        if self._range is not None:
            return self._range
        if data is None:
            data = self._data
        self._range = data[len(data) - 1] - data[0]
        return self._range

    def iqr(self):
        if self._iqr is not None:
            return self._iqr
        self._iqr = self.q3() - self.q1()
        return self._iqr