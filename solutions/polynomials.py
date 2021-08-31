import numpy

def polynomials():

    a = list(map(float, input().split()))
    print(numpy.polyval(a, float(input())))