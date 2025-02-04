import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Define a function for convolution
def compute_convolution(signal1, signal2):
    conv_result = convolve(signal1, signal2, mode='full', method='auto')
    return conv_result

# Sampling frequency and time vector
fs = 1000  # Sampling frequency in Hz
t = np.linspace(0, 1, fs, endpoint=False)  # Time vector
freq = 5  # Frequency of the sine wave

# Generate a sinusoidal signal
sin_signal = np.sin(2 * np.pi * freq * t)

# Example 1: Autoconvolution of a sinusoidal signal
conv_auto = compute_convolution(sin_signal, sin_signal)

plt.figure(figsize=(12, 6))
plt.plot(conv_auto)
plt.title("Autoconvolution of a Sinusoidal Signal")
plt.xlabel("Samples")
plt.ylabel("Convolution Output")
plt.grid()
plt.show()

# Example 2: Convolution with a shifted version
signal1 = sin_signal  # Original sinusoidal signal
signal2 = np.roll(signal1, 100)  # Shifted version

conv_shifted = compute_convolution(signal1, signal2)

plt.figure(figsize=(12, 6))
plt.plot(conv_shifted)
plt.title("Convolution between Signal and Shifted Version")
plt.xlabel("Samples")
plt.ylabel("Convolution Output")
plt.grid()
plt.show()

# Example 3: Convolution with a noisy signal
noise = np.random.normal(0, 0.5, fs)  # Additive Gaussian noise
noisy_signal = signal1 + noise

conv_noisy = compute_convolution(signal1, noisy_signal)

plt.figure(figsize=(12, 6))
plt.plot(conv_noisy)
plt.title("Convolution with Noisy Signal")
plt.xlabel("Samples")
plt.ylabel("Convolution Output")
plt.grid()
plt.show()
