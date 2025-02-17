import numpy as np
import matplotlib.pyplot as plt
import math
import cmath
N_FREQUENCY_SAMPLES = 1000
arr_w = np.arange(-math.pi, math.pi, 2*math.pi/N_FREQUENCY_SAMPLES)
arr_Xw = []
arr_PhoBienDo = []
arr_PhoPha = []
for i in range (N_FREQUENCY_SAMPLES):
    w = arr_w[i]
    Xw = cmath.exp(-1j*w/2) + 1
    Aw = abs(Xw)
    Pw = cmath.phase(Xw)
    arr_PhoBienDo.append(Aw)
    arr_PhoPha.append(Pw)
    arr_Xw.append(Xw)
fig, axs = plt.subplots(2)
axs[0].plot(arr_w, arr_Xw)
axs[0].set(ylabel="Phổ biên độ")
axs[0].set_title("Phổ tín hiệu ")
axs[1].set(ylabel="Phổ pha")
axs[1].set_title("Phổ pha")
axs[1].plot(arr_w, arr_PhoPha)
plt.show()

