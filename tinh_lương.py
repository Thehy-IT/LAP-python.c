"""Viết chương trình nhập vào số giờ làm mỗi tuần, thù lao trên mỗi giờ làm tiêu chuẩn,
từ đó tính ra số tiền thực lĩnh của nhân viên. Với số giờ tiêu chuẩn mỗi tuần là 40 giờ, và
mỗi giờ vượt chuẩn được trả gấp 1.5 lần so với giờ làm chuẩn."""
def tinh_luong(gio_lam,lương_gio_chuan):#dung de định nghĩa hàm

    gio_lam_them= gio_lam - 40# gio lam thêm
    if gio_lam_them >0 :#đk giờ làm thêm lớn hơn 0
        lương_lam_thêm=gio_lam_them*lương_gio_chuan*1.5
    else:
        lương_lam_thêm =0

    luong=40*lương_gio_chuan#tien luong chuan

    tong_luong=lương_lam_thêm + luong

    return tong_luong

gio_lam=float(input("nhập số giờ làm trong tuần: "))
lương_gio_chuan=float(input("nhập lương chuẩn mỗi giờ: "))

tong_luong=tinh_luong(gio_lam,lương_gio_chuan)
print("tiền công nhận được là: ", tong_luong)

