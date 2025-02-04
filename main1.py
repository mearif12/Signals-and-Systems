import numpy as np
import matplotlib.pyplot as plt

# Define the range
n = np.arange(-10, 11)

def impulse_signal(n):
    return np.where(n == 0, 1, 0)

def step_signal(n):
    return np.where(n >= 0, 1, 0)

def ramp_signal(n):
    return np.where(n >= 0, n, 0)

# Generate signals
impulse = impulse_signal(n)
step = step_signal(n)
ramp = ramp_signal(n)

# Plot signals
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.stem(n, impulse)
plt.title("Impulse Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(1, 3, 2)
plt.stem(n, step)
plt.title("Step Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(1, 3, 3)
plt.stem(n, ramp)
plt.title("Ramp Signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
