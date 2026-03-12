def thong_ke_tuple(number):
    if not number:
        return 0, None, None
    tong=sum(number)
    lon_nhat=max(number)
    nho_nhat=min(number)
    return tong, lon_nhat, nho_nhat
my_tuple=(10,25,5,40,30)
tong, max_val, min_val = thong_ke_tuple(my_tuple)
print(f"Tong: {tong}")
print(f"Gia Tri Lon Nhat: {max_val}")
print(f"gia Tri Nho Nhat: {min_val}")
