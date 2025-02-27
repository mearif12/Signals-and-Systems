import numpy as np
import matplotlib.pyplot as plt

def DFT(x):
    """Compute the Discrete Fourier Transform (DFT) of a 1D signal."""
    N = len(x)
    k = np.arange(N).reshape((N, 1))  # Column vector
    n = np.arange(N)  # Row vector
    exp_term = np.exp(-2j * np.pi * k * n / N)
    return np.dot(exp_term, x)  # Matrix multiplication for efficiency

# Sampling parameters
Fs = 1000  
t = np.linspace(0, 1, Fs, endpoint=False)  

# Generate a signal with 50 Hz and 120 Hz sine waves
signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# Compute DFT and frequency bins
dft_output = DFT(signal)
freqs = np.fft.fftfreq(len(dft_output), 1 / Fs)

# Plot single-sided magnitude spectrum
plt.figure(figsize=(10, 5))
plt.plot(freqs[:Fs//2], np.abs(dft_output[:Fs//2]))  
plt.title("DFT Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()
plt.show()
