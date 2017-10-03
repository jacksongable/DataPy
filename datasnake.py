from StatsCalc import OneVarStatsCalc

print "Enter the data, C to stop. Only integers are supported right now."
data = []

while True:
    integer = raw_input()
    if integer.isalpha():
        if integer == "C" or integer == "c":
            break
        else:
            print "Oops! Invalid option. Try again."
            continue
    data.append(int(integer))

stats = OneVarStatsCalc(data)

print "\nPerfect. Here's some one-variable calculations on this data:\n"
print "Mean\t", stats.mean()
print "Standard Deviation:\t", stats.std_dev()
print "Minimum:\t", stats.min()
print "First Quartile:\t", stats.q1()
print "Median:\t", stats.median()
print "Third Quartile:\t", stats.q3()
print "Maximum:\t", stats.max()
print "Range:\t", stats.range()
print "Interquartile range:\t", stats.iqr()

