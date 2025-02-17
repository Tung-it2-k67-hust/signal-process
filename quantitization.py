import numpy as np
import matplotlib.pyplot as plt
import math
#this code include 128, 256 and 512 levels
def quantization(x, n):
    delta = 2 / n  # Tính độ rộng của mỗi mức lượng tử
    x_q = np.round(x / delta) * delta  # Lượng tử hóa tín hiệu
    return x_q

t = np.arange(0, 200, 1)

# Tạo tín hiệu sóng sine với tần số 50
x = np.sin(2 * t * np.pi / 50)

# Lượng tử hóa tín hiệu với các mức khác nhau
n_levels_list = [128, 256, 512]

for n_levels in n_levels_list:
    x_q = quantization(x, n_levels)

    # Tính nhiễu e_q
    e_q = x_q - x

    # Tính công suất của tín hiệu và nhiễu
    P_q = np.mean(e_q ** 2)
    print(f"Power of the noise (P_q) for {n_levels} levels:", P_q)

    P_x = np.mean(x ** 2)
    print(f"Power of the signal (P_x) for {n_levels} levels:", P_x)

    # Tính SNR
    if P_q > 0:
        SNR = 10 * math.log10(P_x / P_q)
        print(f"Signal-to-Noise Ratio (SNR) for {n_levels} levels:", SNR, "dB")
    else:
        print(f"Noise power (P_q) is zero for {n_levels} levels, cannot compute SNR.")

    print(f'Signal-to-Noise Ratio in theory (SNR) for {n_levels} levels:', 1.76 + 6.02 * math.log(n_levels, 2), "dB")

    # Vẽ đồ thị
    plt.figure(figsize=(16, 12))

    plt.scatter(t[:51], x[:51], color='red', label='Original Signal')
    plt.step(t[:51], x_q[:51], label='Quantized Signal', color='blue', linestyle='solid')
    plt.plot(t[:51], e_q[:51], color='orange', label='Error Signal')
    plt.scatter(t[:51], x_q[:51], color='blue', alpha=0.5)

    for ti, xi in zip(t[:51:1], x[:51:1]):
        plt.plot([ti, ti], [0, xi], color='gray', linestyle='--', linewidth=0.5)

    ax = plt.gca()
    ax.spines['bottom'].set_position(('data', 0))

    plt.title(f'Original vs Quantized Signal with {n_levels} Levels')
    plt.xlabel('Number of Samples')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()
    plt.show()