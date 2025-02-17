import numpy as np
import matplotlib.pyplot as plt
import random
# Hàm giải phương trình bậc hai để tìm Z1, Z2
def solve_roots(a1, a2):
    delta = a1**2 - 4 * a2
    Z1 = (-a1 + np.sqrt(delta)) / 2
    Z2 = (-a1 - np.sqrt(delta)) / 2
    return Z1, Z2
# Hàm tính các hệ số A, B
# X(Z) = A/(Z-Z1) + B/(Z_Z2)
def compute_coefficients(Z1, Z2):
    A = Z1**2 / (Z1 - Z2)  # Hệ số ứng với Z1
    B = Z2**2 / (Z2 - Z1)  # Hệ số ứng với Z2
    print("Hệ số A:", A)
    print("Hệ số B:", B)
    return A, B
# Hàm tính tín hiệu x(n)
# Biến đổi Z ngược X = A*Z1**(n-1)*u(n-1) + B*Z2**(n-1)*u(n-1)
def compute_signal(A, B, Z1, Z2, n):
    x_n = A * Z1**(n-1) + B * Z2**(n-1)
    x_n[0] = 0
    print("Tín hiệu x(n):", x_n)
    return x_n
# Main
def main(a1, a2, n_max=5):
    # Bước 1: Giải nghiệm của mẫu số
    Z1, Z2 = solve_roots(a1, a2)

    # Bước 2: Tính hệ số A, B
    A, B = compute_coefficients(Z1, Z2)

    # Bước 3: Tính tín hiệu x(n)
    n = np.arange(0, n_max + 1)  # n từ 0 đến n_max
    x_n = compute_signal(A, B, Z1, Z2, n)

    # Bước 4: Vẽ tín hiệu
    plt.stem(n, x_n)
    plt.title(f"Tín hiệu x(n) với a1 = {a1}, a2 = {a2}")
    plt.xlabel("n")
    plt.ylabel("x(n)")
    plt.grid(True)
    plt.show()

# Tham số ví dụ
a1 = -1  # Thay đổi giá trị này
a2 = -2 # Thay đổi giá trị này
main(a1, a2)
