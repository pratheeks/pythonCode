import matplotlib.pyplot as plt
x1 = [0.1, 0.2, 0.3, 0.4]
y1 = [1, 2, 3, 4]

x2 = [0.1, 0.2, 0.3, 0.4]
y2 = [1, 4, 9, 16]

plt.subplot(1, 2, 1)
plt.plot(x1, y1, label='First')
plt.xlabel('X1')
plt.ylabel('Y1')
plt.title('first')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x2, y2, label='Second')
plt.xlabel('X2')
plt.ylabel('Y2')
plt.title('second')
plt.legend()

plt.show()

























# =============================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# 
# 
# x1 = np.linspace(0.0, 5.0)
# x2 = np.linspace(0.0, 2.0)
# 
# y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
# #print(y1)
# y2 = np.cos(2 * np.pi * x2)
# #print(y2)
# 
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, 'p-')
# plt.title('2 plots')
# plt.ylabel('Damped oscillation')
# 
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, '.-')
# plt.xlabel('time (s)')
# plt.ylabel('Undamped')
# 
# plt.show()
# 
# 
# =============================================================================