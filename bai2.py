for i in range (111,16,-2):
    print(i)

print("Các số nguyên tố từ 17 đến 111 là:")

for n in range(17, 112):
    so_nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(n, end=" ")