#
# This class performs 1-variable statistics calculations on the data set it is initialized with.
# Since the data set is immutable, each bound method only runs the necessary calculations once,
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
        self._mean = total / len(self._data)
        return self._mean

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
        if data is None and self._med is not None:
            return self._med
        if data is None:
            data = self._data
        max_index = len(data) - 1

        if len(data) % 2 == 1: #list length is odd
            median = data[max_index / 2]
        else:
            medians = (data[max_index // 2], data[max_index // 2 + 1])
            median = self.mean(medians)
        self._med = median
        return self._med

    def q1(self):
        if self._q1 is not None:
            return self._q1
        if len(self._data) % 2 == 1:
            stop = (len(self._data) - 1) / 2
        else:
            stop = len(self._data) / 2
        self._q1 = self.median(list[0 : stop])
        return self._q1

    def q3(self):
        if self._q3 is not None:
            return self._q3
        if len(self._data) % 2 == 1:
            start = len(self._data) / 2 + 1
        else:
            start = len(self._data) / 2
        self._q3 = self.median(self._data[start : len(self._data)])
        return self._q3

    def range(self, data=None):
        if self._range is not None:
            return self._range
        if data is None:
            data = self._data
        self._range = list[len(data) - 1] - data[0]
        return self._range

    def calc_iqr (self):
        if self._iqr is not None:
            return self._iqr
        self._iqr = self.q3() - self.q1()
        return self._iqr







#Eventually you'll be able to do a lot more cool stuff.

print ("Hi there! Enter the data. 'C' to stop.");

list = []

while True:
    val = raw_input()
    if val == "c" or val == "C":
        break
    elif val.isalpha():
        print("Oops! Not a valid option")
        continue
    list.append(float(val))

calc = OneVariableStatsCalc(list)

print("Q1", calc.q1())
print("Median", calc.median())
print("Q3", calc.q3())