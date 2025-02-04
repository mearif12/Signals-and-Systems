import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate, correlation_lags

# Define a function for autocorrelation
def compute_autocorrelation(signal):
    auto_corr = correlate(signal, signal, mode='full', method='auto')
    lags = correlation_lags(len(signal), len(signal), mode='full')
    return auto_corr, lags

# Define a function for cross-correlation
def compute_cross_correlation(signal1, signal2):
    cross_corr = correlate(signal1, signal2, mode='full', method='auto')
    lags = correlation_lags(len(signal1), len(signal2), mode='full')
    return cross_corr, lags

# Sampling frequency and time vector
fs = 1000  # Sampling frequency in Hz
t = np.linspace(0, 1, fs, endpoint=False)  # Time vector
freq = 5  # Frequency of the sine wave

# Generate a sinusoidal signal
sin_signal = np.sin(2 * np.pi * freq * t)

# Compute and plot autocorrelation
auto_corr, lags = compute_autocorrelation(sin_signal)
plt.figure(figsize=(12, 6))
plt.plot(lags, auto_corr)
plt.title("Autocorrelation of a Sinusoidal Signal")
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.grid()
plt.show()

# Cross-correlation between a signal and its shifted version
signal1 = sin_signal  # Original sinusoidal signal
signal2 = np.roll(signal1, 100)  # Shifted version

cross_corr, lags = compute_cross_correlation(signal1, signal2)
plt.figure(figsize=(12, 6))
plt.plot(lags, cross_corr)
plt.title("Cross-Correlation between Two Signals")
plt.xlabel("Lag")
plt.ylabel("Cross-Correlation")
plt.grid()
plt.show()

# Cross-correlation with noise
noise = np.random.normal(0, 0.5, fs)  # Additive Gaussian noise
noisy_signal = signal1 + noise

cross_corr_noise, lags = compute_cross_correlation(signal1, noisy_signal)
plt.figure(figsize=(12, 6))
plt.plot(lags, cross_corr_noise)
plt.title("Cross-Correlation with Noisy Signal")
plt.xlabel("Lag")
plt.ylabel("Cross-Correlation")
plt.grid()
plt.show()
