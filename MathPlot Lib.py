import matplotlib.pyplot as plt
import numpy as np


Fs = 8000
f = 5
print(type(f))
sample = 100
x = np.arange(sample)
print(type(x))
# y = np.sin(2 * np.pi * f * x / Fs)
y = (0.4 * (1 + np.sin(np.radians(x * 10))))
z = (0.2 * (1 + np.cos(np.radians(x * 10)))) + 0.2
t = (0.1 * (1 + np.sin(np.radians((x + 90) * 10)))) + 0.3
print(type(y))
plt.plot(x, y)
plt.plot(x, z)
plt.plot(x, t)
plt.xlabel('Counter in degrees (Y)')
plt.ylabel('Vo(Turning Factor)')
# plt.zlabel('Lateral Translation Direction (in Degrees)')

plt.show()