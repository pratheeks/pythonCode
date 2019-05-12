
# Python Programming illustrating
# numpy.arange method

""" start : [optional] start of interval range. By default start = 0
    stop  : end of interval range
    step  : [optional] step size of interval. By default step size = 1,
    For any output out, this is the distance between two adjacent values, out[i+1] - out[i].
    dtype : type of output array  """

import numpy as geek

print("A\n", geek.arange(4).reshape(2, 2), "\n")

print("A\n", geek.arange(4, 10), "\n")

print("A\n", geek.arange(4, 20, 3), "\n")