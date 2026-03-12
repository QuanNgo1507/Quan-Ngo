sinh_vien = {
    "An": 8.5,
    "Bình": 7.0,
    "Cường": 9.0
}
ten_can_tim = "Bình"
if ten_can_tim in sinh_vien:
    print(f"Tìm thấy sinh viên {ten_can_tim}, điểm số là: {sinh_vien[ten_can_tim]}")
else:
    print(f"Không tìm thấy sinh viên {ten_can_tim} trong danh sách.")