import numpy as np
import matplotlib.pyplot as plt

# Input sequence and N
x = list(map(float, input("Enter the sequence x(n): ").split()))
N = int(input("Input N: "))

# Zero-padding if needed
x = np.pad(x, (0, N - len(x)), mode='constant')

# DFT computation
X = np.fft.fft(x, N)

# IDFT computation (Inverse DFT)
x_reconstructed = np.fft.ifft(X)

# Print the DFT and IDFT values
print("DFT values:", X)
print("Reconstructed IDFT values:", x_reconstructed.real)

# Plot the input signal
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.stem(range(len(x)), x)
plt.title('Input Signal x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid()

# Plot the magnitude of DFT
plt.subplot(3, 1, 2)
plt.stem(range(N), np.abs(X))
plt.title('DFT Magnitude |X(k)|')
plt.xlabel('k')
plt.ylabel('|X(k)|')
plt.grid()

# Plot the IDFT signal
plt.subplot(3, 1, 3)
plt.stem(range(N), x_reconstructed.real)
plt.title('Reconstructed Signal x(n) from IDFT')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid()

plt.tight_layout()
plt.show()
