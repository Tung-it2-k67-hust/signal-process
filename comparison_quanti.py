import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.io import wavfile
from scipy.signal import resample

"""## Đọc file wave"""
file_path = 'sample.wav'
sample_rate, audio_data = wavfile.read(file_path)

# Tính thời gian file âm thanh
duration = len(audio_data) / sample_rate

"""## Hàm lượng tử hóa tín hiệu"""
def quantization(x, n):
    x = np.asarray(x, dtype=np.float64)
    x_min, x_max = np.min(x), np.max(x)

    # Tính độ rộng của mỗi mức lượng tử
    delta = (x_max - x_min) / n

    # Lượng tử hóa tín hiệu
    x_q = np.round((x - x_min) / delta) * delta + x_min

    return x_q

"""## Tín hiệu lấy mẫu, tín hiệu lượng tử và sai số lượng tử"""
t = np.arange(0, 200, 1)
x = audio_data[:, 0]

# Lượng tử hóa tín hiệu với n mức
n_levels = 256
x_q = quantization(x, n_levels)

# Tính nhiễu e_q
e_q = x_q - x

# Lưu file mới sau khi lượng tử hóa
output_file = f'sampled_audio_{n_levels}levels.wav'
wavfile.write(output_file, sample_rate, x_q.astype(np.int16))

"""## Công suất tín hiệu, công suất lỗi và SNR"""
# Tính công suất của tín hiệu và nhiễu
p_x = np.sum(x ** 2)
p_e = np.sum(e_q ** 2)

print("Power of the signal (P_x):", p_x)
print("Power of the noise (P_e):", p_e)

# Tính SNR
SNR = 10 * np.log10(p_x / p_e)
print("Signal-to-Noise Ratio (SNR):", SNR, "dB")
print('Signal-to Noise Ratio in theory (SNR): ', 1.76 + 6.02 * math.log(n_levels, 2), "dB")

"""## Vẽ đồ thị"""
plt.figure(figsize=(12, 8))
plt.suptitle(f'Original vs Quantized Signal with {n_levels} Levels (SNR = {SNR:.2f} dB)', fontsize=16)

# Biểu đồ 1: Tín hiệu gốc
plt.subplot(2, 2, 1)
plt.plot(x, label='Original Signal', color='red')
plt.title('Original Signal')
plt.xlabel('Number of Samples')
plt.ylabel('Amplitude')
plt.legend()

# Biểu đồ 2: Tín hiệu đã lượng tử hóa
plt.subplot(2, 2, 2)
plt.plot(x_q, label='Quantized Signal', color='blue')
plt.title('Quantized Signal')
plt.xlabel('Number of Samples')
plt.ylabel('Amplitude')
plt.legend()

# Biểu đồ 3: Tín hiệu lỗi
plt.subplot(2, 2, 3)
plt.plot(e_q, label='Error Signal', color='green')
plt.title('Error Signal')
plt.xlabel('Number of Samples')
plt.ylabel('Amplitude')
plt.legend()

# Tối ưu hóa bố cục để không bị chồng chéo
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Để lại khoảng trống cho tiêu đề chính

# Hiển thị biểu đồ
plt.show()

"""### Xem kĩ hơn một phần đồ thị"""
start_time = 1.0  # Thời gian bắt đầu (giây)
end_time = 1.02  # Thời gian kết thúc (giây)

# Tính toán số mẫu tương ứng với thời gian bắt đầu và kết thúc
start_sample = int(start_time * sample_rate)
end_sample = int(end_time * sample_rate)
print(start_sample, end_sample)

# Chọn đoạn dữ liệu từ 1s đến 1.04s
x1 = x[start_sample:end_sample]
x_q1 = x_q[start_sample:end_sample]
e_q1 = e_q[start_sample:end_sample]

# Vẽ đồ thị
plt.figure(figsize=(12, 8))
plt.plot(t[:200], x1[:200], color='red', label='Original Signal')
plt.step(t[:200], x_q1[:200], label='Quantized Signal', color='blue', linestyle='solid')
plt.plot(t[:200], e_q1[:200], color='orange', label='Error Signal')
plt.scatter(t[:200], x_q1[:200], color='blue', alpha=0.5)
for ti, xi in zip(t[:200:1], x1[:200:1]):
    plt.plot([ti, ti], [0, xi], color='gray', linestyle='--', linewidth=0.5)

ax = plt.gca()
ax.spines['bottom'].set_position(('data', 0))
plt.title(f'Original vs Quantized Signal with {n_levels} Levels (SNR = {SNR}dB)')
plt.xlabel('Number of Samples')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
plt.show()