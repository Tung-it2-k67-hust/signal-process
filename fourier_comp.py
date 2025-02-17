import numpy as np
import matplotlib.pyplot as plt

# Define parameters
T0 = 2 * np.pi  # Period of the signal
omega_0 = 2 * np.pi / T0  # Fundamental frequency
t = np.linspace(0, T0, 1000)  # Create time array

# Function to synthesize square wave from N Fourier components
def square_wave(N):
    x_t = np.zeros_like(t)
    for n in range(1, N + 1, 2):  # Use odd frequency components
        x_t += (4 / (n * np.pi)) * np.sin(n * omega_0 * t)
    return x_t

# Plot the signal for N = 1, 5, 50
plt.figure(figsize=(10, 6))

for N in [1, 5, 50]:
    x_t = square_wave(N)
    plt.plot(t, x_t, label=f'N = {N}')

plt.title("Periodic Continuous Square Wave Synthesized from N Components")
plt.xlabel("Time (t)")
plt.ylabel("Value x(t)")
plt.legend()
plt.grid(True)
plt.show()