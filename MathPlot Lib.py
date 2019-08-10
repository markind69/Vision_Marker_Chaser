import matplotlib.pyplot as plt
import numpy as np


Fs = 8000
f = 5
print(type(f))
sample = 100
x = np.arange(sample)
print(type(x))
# y = np.sin(2 * np.pi * f * x / Fs)
y = (0.3 * (1 + np.sin(np.radians(x * 10))))
t = (0.3 * (1 + np.cos(np.radians(x * 10))))
print(type(y))
plt.plot(x, y)
plt.plot(x, t)
plt.xlabel('Counter in degrees (Y)')
plt.ylabel('Vo(Turning Factor)')
plt.tlabel('Lateral Translation Direction (in Degrees)')

plt.show()