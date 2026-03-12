danh_sach_lop = {
    "Nguyen Van A": 9.5,
    "nguyen Van B":7.5,
    "Nguyen Van C": 8.0
}
def tinh_diem_trung_binh(data_dict):
    if not data_dict:
        return 0
    Tong_Diem=sum(data_dict.values())
    So_Luong_SV=len(data_dict.keys())
    return Tong_Diem / So_Luong_SV
dtb = tinh_diem_trung_binh(danh_sach_lop)
print(f"Diem trung Binh cua {len(danh_sach_lop)} sinh vien la {dtb:.2f}")
