import sys
import numpy


def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = numpy.loadtxt(filename, delimiter=',')
    for row_mean in data.mean(axis=1):
        print(row_mean)
