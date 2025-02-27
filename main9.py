import numpy as np

# Define parameters
N = 1024   # Number of points in DFT
Fs = 1000  # Sampling frequency (Hz)

# Compute frequency bins manually
freq_bins = np.array([(k / N) * Fs for k in range(N)])
# # Compute frequency bins using NumPy
# freq_bins = np.fft.fftfreq(N, d=1/Fs)

print(freq_bins[:10])  # Print first 10 frequency bins
