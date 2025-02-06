import numpy as np
import matplotlib.pyplot as plt

# Define time range
t = np.arange(-2, 2.01, 0.01)  # Equivalent to -2:0.01:2 in MATLAB

# Compute function x(t) = 4 * sinc(4 * π * t)
x = 4 * np.sinc(4 * t)  # sinc(x) in NumPy is sin(πx)/(πx), so no need for π in input

# Plot real part
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Real Part')
plt.grid()

# Plot phase part
plt.subplot(3, 1, 2)
plt.plot(t, np.angle(x))  # Angle (phase) of x
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Phase Part')
plt.grid()

# Plot magnitude part
plt.subplot(3, 1, 3)
plt.plot(t, np.abs(x))  # Magnitude of x
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Magnitude Part')
plt.grid()

plt.tight_layout()
plt.show()
