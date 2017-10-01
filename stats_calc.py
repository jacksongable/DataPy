class OneVariableStatsCalc:

    __data = []

    def __init__(self, data):
        data.sort()
        self.__data = data

    def calc_mean (self, data=None):
        if data is None:
            data = self.__data
        total = 0
        for x in data:
            total += x
        return total / len(self.__data)

    def calc_max (self):
        current_max = self.__data[0]
        for element in self.__data:
            if element > current_max:
                current_max = element
        return current_max

    def calc_min (self):
        current_min = self.__data[0]
        for element in self.__data:
            if element < current_min:
                current_min = element
        return current_min

    def calc_median(self, data=None):
        if data is None:
            data = self.__data
        max_index = len(data) - 1

        if len(data) % 2 == 1: #list length is odd
            median = data[max_index / 2]
        else:
            medians = (data[max_index // 2], data[max_index // 2 + 1])
            median = self.calc_mean(medians)
        return median

    def calc_q1(self):
        if len(self.__data) % 2 == 1:
            stop = (len(self.__data) - 1) / 2
        else:
            stop = len(self.__data) / 2
        return self.calc_median(list[0 : stop])

    def calc_q3(self):
        if len(self.__data) % 2 == 1:
            start = len(self.__data) / 2 + 1
        else:
            start = len(self.__data) / 2
        return self.calc_median(self.__data[start : len(self.__data)])

    def calc_range(self, data=None):
        if data is None:
            data = self.__data
        return list[len(data) - 1] - data[0]

    def calc_iqr (self):
        return self.calc_q3() - self.calc_q1();







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

#print("Mean", calc.calc_mean())
#print("Minimum", calc.calc_min())
print("Q1", calc.calc_q1())
print("Median", calc.calc_median())
print("Q3", calc.calc_q3())
#print("Maximum", calc.calc_max())
#print("\n")
#print("Range", calc.calc_range())
#0print("Interquartile Range", calc.calc_iqr())