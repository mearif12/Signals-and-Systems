import numpy as np
import matplotlib.pyplot as plt

# Function to add two signals
def signal_addition(x1, x2):
    return x1 + x2

# Function to multiply two signals
def signal_multiplication(x1, x2):
    return x1 * x2

# Function to scale a signal
def signal_scaling(x, alpha):
    return alpha * x

# Function to shift indices only (not the amplitude)
def signal_shifting(n, shift):
    return n + shift  # Only shift the indices

# Function to fold (reverse) a signal
def signal_folding(x):
    return np.flip(x)  # Flip both values & indices

# Example signal
n = np.array([-2, -1, 0, 1, 2])  # Time indices
x1 = np.array([1, 2, 3, 4, 5])   # First signal
x2 = np.array([5, 4, 3, 2, 1])   # Second signal

# Perform operations
added_signal = signal_addition(x1, x2)
multiplied_signal = signal_multiplication(x1, x2)
scaled_signal = signal_scaling(x1, 2)
shifted_signal1 = signal_shifting(n, -2)  # Shifted indices only
shifted_signal2 = signal_shifting(n, +2)  # Shifted indices only
folded_signal = signal_folding(x1)  # Folded indices

# Plot the results
plt.figure(figsize=(12, 10))

plt.subplot(4, 2, 1)
plt.stem(n, x1)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Original Signal x1")
plt.grid()

plt.subplot(4, 2, 2)
plt.stem(n, x2)
plt.xlabel("Time ")
plt.ylabel("Amplitude")
plt.title("Original Signal x2")
plt.grid()

plt.subplot(4, 2, 3)
plt.stem(n, added_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal Addition")
plt.grid()

plt.subplot(4, 2, 4)
plt.stem(n, multiplied_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal Multiplication")
plt.grid()

plt.subplot(4, 2, 5)
plt.stem(n, scaled_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Scaled Signal (x1 * 2)")
plt.grid()

plt.subplot(4, 2, 6)
plt.stem(shifted_signal1, x1) 
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Shifted Signal (Shift = -2)")
plt.grid()

plt.subplot(4, 2, 7)
plt.stem(shifted_signal2,x1) 
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Shifted Signal (Shift = +2)")
plt.grid()

plt.subplot(4, 2, 8)
plt.stem(n, folded_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")  
plt.title("Folded Signal (x1)")
plt.grid()

plt.tight_layout()
plt.show()
