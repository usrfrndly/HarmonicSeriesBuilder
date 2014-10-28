'''
HarmonicSeriesTest.py : A test suite that compares values actual values derived from the HarmonicSeries class
to a CSV file containing the expected values
The base frequency noted in the main method of HarmonicSeries.py should equal the basefrequency in the csv file

Jaclyn Horowitz
Music Software 2014
'''
import csv

# Change csv file to be compared to here
my_file = open('harmonic_series.csv', 'rU')
my_file.seek(0)
csv_list = list(csv.reader(my_file))
# How many header rows to skip
header_cnt = 0
# Skip header rows
for row in csv_list:
    if not row[0] == '1':
        header_cnt += 1
    elif row[0] == '1':
        # base_fq = float(row[8])
        # print("The base fq is ", base_fq)
        break
csv_list = csv_list[header_cnt:]
my_file.close()

# test_all_cells(harmonic_series): accepts a HarmonicSeries object as a parameter and compares
# every property in each calculated interval row to the corresponding row and cell in a csv file
def test_all_cells(harmonic_series):
    print("*** Beginning test_all_cells() tests ***")
    failed = 0
    # Iterate through each row in the csv file
    for r in csv_list:
        # print r
        # The harmonic interval of the row
        csv_interval = int(r[0])
        harmonic_series_row = harmonic_series.series_rows[csv_interval-1].to_array()
        for i in range(0, len(r)):
            # Exception will be thrown for ratio properties, because they cannot be coverted to floats
            # Instead we will compare the calculated and csv cell as string representations
            try:
                #print("Testing " + str(csv_interval) + ":" + str(i))
                if float(harmonic_series_row[i]) != float(r[i]):
                    print("INCORRECT: For Interval %d and Column %d. CSV Cell = %s , Calculated  = %s" % (
                        csv_interval, i, str(r[i]), str(harmonic_series_row[i])))
                    failed += 1
                else:
                    print("Correct: Interval " + str(csv_interval) + ": Cell " + str(i) + ". For Value: " + str(harmonic_series_row[i]))
            except ValueError:
                if str(harmonic_series_row[i]) != str(r[i]):
                    print("INCORRECT: For Interval %d and Column %d. CSV Cell = %s , Calculated  = %s" % (
                        csv_interval, i, str(r[i]), str(harmonic_series_row[i])))
                    failed += 1
                else:
                    print("Correct: Interval " + str(csv_interval) + ": Cell " + str(i) + ". For Value: " + str(harmonic_series_row[i]))


    print("*** test_all_cells() SUMMARY *** ")
    print("Failed: %d " % failed)


# test_frequency(): Tests the get_frequency() function in the HarmonicSeries
# class by comparing the calculated values with the expected values in the csv file
def test_frequency(harmonic_scale):
    print("*** Beginning test_frequency() tests ***")
    failed = 0
    # Iterate through each row in the csv file
    for r in csv_list:
        # print r
        # The harmonic interval of the row
        csv_interval = int(r[0])
        # Frequency calculated by get_frequency() function in HarmonicSeries class
        calculated_frequency = harmonic_scale.get_frequency(csv_interval)
        # Frequency found in csv
        csv_frequency = int(r[2])
        if csv_frequency == calculated_frequency:
            print("CORRECT: Frequency for Interval %d = %d" % (csv_interval, calculated_frequency))
        elif csv_frequency != calculated_frequency:
            print("INCORRECT: Frequency for Interval %d . CSV Frequency = %d , " \
                  "Calculated Frequency = %d" % (csv_interval, csv_frequency, calculated_frequency))
            failed += 1
    print("*** test_frequency() SUMMARY *** ")
    print("Failed: %d . Successful: %d ." % (failed, len(csv_list) - failed))


# test_ratio(): Tests the get_ratio() function in the HarmonicSeries
# class by comparing the calculated values with the expected values in the csv file
def test_ratio(harmonic_scale):
    print("*** Beginning test_ratio() ***")
    failed = 0
    for r in csv_list:
        # The harmonic interval the corresponds with the row
        csv_interval = int(r[0])
        # Ratio calculated by get_ratio() function in HarmonicSeries class
        calculated_ratio = harmonic_scale.get_ratio(csv_interval)
        # Ratio found in csv
        csv_ratio = r[5]
        if csv_ratio == calculated_ratio:
            print("CORRECT: Ratio for Interval %d = %s" % (csv_interval, calculated_ratio))
        elif csv_ratio != calculated_ratio:
            print("INCORRECT: Ratio for Interval %d . CSV Ratio = %s , Calculated Ratio = %s" % (
                csv_interval, csv_ratio, calculated_ratio))
            failed += 1
    print("*** test_ratio() SUMMARY *** ")
    print("Failed: %d . Successful: %d ." % (failed, len(csv_list) - failed))
