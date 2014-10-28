"""
HarmonicSeriesRow.py
Jaclyn Horowitz
Music Software Projects 2014
"""

import math
from fractions import gcd

'''
HarmonicSeriesRow class : Represents an interval row in the harmonic series and is initialized with a
harmonic interval degree and a base frequency.
'''


class HarmonicSeriesRow:
    def __init__(self, interval, basefrq):
        self.base_frequency = basefrq
        self.interval = int(interval)
        self.freqtofundamental = self.get_frequencytofundamental()
        self.frequency = self.get_frequency()
        self.octave = self.get_octave()
        self.denom = self.get_denom()
        self.ratio = self.get_ratio()
        self.ratio_reduced = self.get_ratio_reduced()
        self.decimal_num = self.get_decimal()
        self.freqlowestoctave = self.get_freqlowestoctave()

    '''
    Methods that calculate properties for a row in the HarmonicSeries
    '''

    def get_frequencytofundamental(self):
        return "\"" + str(self.interval) + "/1\""

    def get_octave(self):
        return math.floor(math.log(self.interval, 2)) + 1

    def get_denom(self):
        return int(math.pow(2, self.octave - 1))

    # get_frequency(interval) : Accepts a harmonic interval as a parameter and returns the corresponding frequency
    def get_frequency(self):
        hertz = int(self.base_frequency * self.interval)
        return hertz

    # get_ratio(interval) : Accepts a harmonic interval as a parameter and returns the ratio of
    # the interval to its lowest octave
    def get_ratio(self):
        # octave = math.floor(math.log(self.interval, 2)) + 1
        # denom = int(math.pow(2, octave - 1))
        return "\"" + str(self.interval) + "/" + str(self.denom) + "\""

    def get_ratio_reduced(self):
        # octave = math.floor(math.log(self.interval, 2)) + 1
        # denom = int(math.pow(2, octave - 1))
        gcdenom = gcd(self.interval, self.denom)
        if gcdenom > 1:
            new_interval = self.interval / gcdenom
            new_demon = self.denom / gcdenom
            return "\"" + str(int(new_interval)) + "/" + str(int(new_demon)) + "\""
        return "\"" + str(self.interval) + "/" + str(self.denom) + "\""

    def get_decimal(self):
        dec = float(self.interval) / float(self.denom)
        return format(float(dec), '.5f')

    def get_freqlowestoctave(self):
        return float(self.decimal_num) * self.base_frequency


    # to_array(): Returns an array representation of the properties of a row in the HarmonicSeries, which
    # orders the properties the same as in the csv file
    def to_array(self):
        return [self.interval, self.freqtofundamental, self.frequency, self.octave, self.denom, self.ratio,
                self.ratio_reduced, self.decimal_num, self.freqlowestoctave]

    # show_row(): Returns a string representation of the properties of a row in the HarmonicSeries
    def show_row(self):
        # [interval, frequencytofundamental, frequency, octave, denom, ratio, ratio_reduced, decimal,freqinlowestoctave]
        print("[{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}] ".format(str(self.interval), self.freqtofundamental,
                                                                      str(self.frequency), str(
                self.octave), str(self.denom), self.ratio, self.ratio_reduced, str(self.decimal_num),
                                                                      str(self.freqlowestoctave)))