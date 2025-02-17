import numpy as np
import scipy.io.wavfile as wav
def filter_noise(input_file, N):
  #Đọc file âm thanh
  sample_rate, data = wav.read(input_file)

  #Chuyển file âm thanh thành dạng mảng
  data = data.astype(np.float64)

  #Mảng đầu ra
  filtered_data = np.zeros_like(data)

  #Lọc nhiễu
  for i in range(N, len(data) - N):
    filtered_data[i] = data[i]
    for j in range(1,N):
      if i-j>=0:
        filtered_data[i] += data[i-j]
    filtered_data /= N

  # Chuyển đổi lại dữ liệu thành kiểu int16
  filtered_data = filtered_data.astype(np.int16)

  # Ghi âm thanh đã lọc ra file mới
  output_file = f"N{N}.wav"
  wav.write(output_file, sample_rate, filtered_data)

  return output_file
# N levels
N_values = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
input_file = '64levels.wav'

# Lọc nhiễu cho từng giá trị N
for N in N_values:
    output_file = filter_noise(input_file, N)
    print(f"Filtered audio saved to: {output_file}")