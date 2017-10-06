from StatsCalc import OneVarStatsCalc


#  Prints each option
def print_options():
    print "Enter a number to perform calculation."
    print "1.\tMean"
    print "2.\tStandard Deviation"
    print "3.\tRange"
    print "4.\tInterquartile Range"
    print "5.\tMinimum"
    print "6.\tLower Fence"
    print "7.\tFirst Quartile"
    print "8.\tMedian"
    print "9.\tThird Quartile"
    print "10.\tUpper Fence"
    print "11.\tMaximum"
    print "12.\tOutliers"
    print "13.\tQuit\n"


#  Reads, validates, and returns the user's selection
def parse_selection():
    while True:
        choice = raw_input()
        valid = False
        if choice.isdigit():
            if 0 < int(choice) < 14:
                valid = True
        if not valid:
            print "Oops! Invalid entry."
            continue
        else:
            return int(choice)


print "Enter the data, C to stop. Only integers are supported right now."
data = []


#  Loop that initializes data list
while True:
    integer = raw_input()
    if integer.isalpha():
        if integer == "C" or integer == "c":
            break
        else:
            print "Oops! Invalid option. Try again."
            continue
    data.append(int(integer))

print "Calculations will be performed on the following data set: ", data

stats = OneVarStatsCalc(data)

print_options()

#  Performs calculation specified by user in parse_selection
while True:
    selection = parse_selection()

    if selection == 1:
        print "Mean\t", stats.mean()
    elif selection == 2:
        print "Standard Deviation:\t", stats.std_dev()
    elif selection == 3:
        print "Range:\t", stats.range()
    elif selection == 4:
        print "Interquartile range:\t", stats.iqr()
    elif selection == 5:
        print "Minimum:\t", stats.min()
    elif selection == 6:
        print "Lower fence:\t", stats.lower_fence()
    elif selection == 7:
        print "First Quartile:\t", stats.q1()
    elif selection == 8:
        print "Median:\t", stats.median()
    elif selection == 9:
        print "Third Quartile:\t", stats.q3()
    elif selection == 10:
        print "Upper fence:\t", stats.upper_fence()
    elif selection == 11:
        print "Maximum:\t", stats.max()
    elif selection == 12:
        print "Outliers:\t", stats.outliers()
    elif selection == 13:
        print "Exiting."
        exit(0)
