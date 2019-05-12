# Python program explaining
# sin() function

import numpy as np
import math

in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print("Input array : \n", in_array)

Sin_Values = np.sin(in_array)
print("\nSine values : \n", Sin_Values)

# Python program showing
# Graphical representation of
# sin() function

import numpy as np
import matplotlib.pyplot as plt

in_array = np.linspace(-np.pi, np.pi, 12)
out_array = np.sin(in_array)

print("\nin_array : \n", in_array)
print("\nout_array : ", out_array)

# red for numpy.sin()
plt.plot(in_array, out_array, color='red', marker="x")
plt.title("numpy.sin()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()