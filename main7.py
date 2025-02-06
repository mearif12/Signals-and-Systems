import numpy as np
import matplotlib.pyplot as plt

# Fourier series approximation of a square wave
def fourier_series(x, terms):
    if terms < 1:
        raise ValueError("Number of terms must be at least 1")
    
    result = x - x  # Start from zero
    for n in range(1, terms + 1, 2):  # Use only odd harmonics
        result += (4 / (np.pi * n)) * np.sin(n * x)  # Sum sine terms
    return result

# Define the original square wave function
def square_wave(x):
    return np.where(np.sin(x) >= 0, 1, -1)  # Standard square wave

# Generate x values
t = np.linspace(-np.pi, np.pi, 400)

# Plot different approximations
plt.figure(figsize=(8, 6))

# Plot the original square wave
plt.plot(t, square_wave(t), label='Original Square Wave', linestyle='--', color='black')

for terms in [1, 3, 5, 11]:
    plt.plot(t, fourier_series(t, terms), label=f'{terms} terms')

plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.title('Fourier Series Approximation of a Square Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
