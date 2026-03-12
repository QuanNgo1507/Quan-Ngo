class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return f"Hoa {self.ten} có màu {self.mau}."
hoa_cua_toi = Hoa("Hồng", "Đỏ rực")
print(hoa_cua_toi)