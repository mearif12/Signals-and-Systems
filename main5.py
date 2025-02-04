import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def bandpass_filter(data, fs=100):
    b, a = signal.butter(4, [0.5 / (0.5 * fs), 5.0 / (0.5 * fs)], btype='band')
    return signal.filtfilt(b, a, data)

def detect_peaks(signal_data):
    return signal.find_peaks(signal_data, distance=50)[0]

def extract_heart_rate(peaks, fs=100):
    if len(peaks) < 2:
        return 0
    rr_intervals = np.diff(peaks) / fs
    return 60 / np.mean(rr_intervals)

# Generate synthetic PPG signal
fs = 100
t = np.linspace(0, 10, fs * 10)
sine_signal = np.sin(2 * np.pi * 1.2 * t)
noise_signal = 0.1 * np.random.normal(0, 1, len(t))
ppg_signal = sine_signal + noise_signal

# Process PPG signal
filtered_signal = bandpass_filter(ppg_signal, fs)
normalized_signal = (filtered_signal - np.min(filtered_signal)) / (np.max(filtered_signal) - np.min(filtered_signal))
peaks = detect_peaks(normalized_signal)
heart_rate = extract_heart_rate(peaks, fs)

# Print results
print("Filtered Signal (first 10 values):", filtered_signal[:10])
print("Detected Peaks (first 10 indices):", peaks[:10])
print(f"Estimated Heart Rate: {heart_rate:.2f} BPM")

# Plot results
plt.figure(figsize=(12, 9))
plt.subplot(3, 2, 1)
plt.plot(t, sine_signal, label='Raw Sine Signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(3, 2, 2)
plt.plot(t, noise_signal, label='Raw Noise Signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(3, 2, 3)
plt.plot(t, ppg_signal, label='Raw PPG Signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(3, 2, 4)
plt.plot(t, filtered_signal, label='Filtered PPG Signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(3, 2, 5)
plt.plot(t, normalized_signal, label='Normalized PPG Signal')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(3, 2, 6)
plt.plot(t, normalized_signal,label=f'PPG with Detected Peaks(HR: {heart_rate:.2f} BPM)')
plt.plot(t[peaks], normalized_signal[peaks],'ro', label='Detected Peaks')
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
