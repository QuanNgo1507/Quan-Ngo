a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)
print(f"Số lớn nhất là: {so_lon_nhat}")
print(f"Số nhỏ nhất là: {so_nho_nhat}")

import math
def giai_phuong_trinh_bac_2(a, b, c):
    if a == 0:
        return "Hệ số a phải khác 0!"
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phương trình có nghiệm kép x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Phương trình có 2 nghiệm: x1 = {x1}, x2 = {x2}"
print(giai_phuong_trinh_bac_2(1,4,3))