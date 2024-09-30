'''Viết chương trình quản lý sinh viên đơn giản gồm các thông tin mssv, họ tên, điểm
số sử dụng list trong Python bao gồm các tính năng sau:
- Thêm sinh viên(người dùng nhập)
- Hiển thị danh sách sinh viên
- Hiển thị danh sách sinh viên có điểm số > 7
- Tìm kiếm sinh viên theo mssv
- Cập nhật điểm số của sinh viên
- Xóa sinh viên theo mssv'''
# Khởi tạo danh sách sinh viên
danh_sach_sinh_vien = []

# Hàm thêm sinh viên
def them_sinh_vien():
    mssv = input("Nhập MSSV: ")
    ho_ten = input("Nhập họ tên: ")
    diem = float(input("Nhập điểm số: "))
    sinh_vien = {'MSSV': mssv, 'Ho Ten': ho_ten, 'Diem': diem}
    danh_sach_sinh_vien.append(sinh_vien)
    print("Thêm sinh viên thành công!\n")

# Hàm hiển thị danh sách sinh viên
def hien_thi_danh_sach_sinh_vien():
    if danh_sach_sinh_vien:
        print("Danh sách sinh viên:")
        for sv in danh_sach_sinh_vien:
            print(f"MSSV: {sv['MSSV']}, Họ tên: {sv['Ho Ten']}, Điểm: {sv['Diem']}")
    else:
        print("Danh sách sinh viên rỗng.\n")

# Hàm hiển thị danh sách sinh viên có điểm số > 7
def hien_thi_sinh_vien_diem_cao():
    print("Danh sách sinh viên có điểm số > 7:")
    found = False
    for sv in danh_sach_sinh_vien:
        if sv['Diem'] > 7:
            print(f"MSSV: {sv['MSSV']}, Họ tên: {sv['Ho Ten']}, Điểm: {sv['Diem']}")
            found = True
    if not found:
        print("Không có sinh viên nào có điểm số > 7.\n")

# Hàm tìm kiếm sinh viên theo MSSV
def tim_kiem_sinh_vien():
    mssv = input("Nhập MSSV cần tìm: ")
    for sv in danh_sach_sinh_vien:
        if sv['MSSV'] == mssv:
            print(f"Thông tin sinh viên:\nMSSV: {sv['MSSV']}, Họ tên: {sv['Ho Ten']}, Điểm: {sv['Diem']}")
            return
    print("Không tìm thấy sinh viên có MSSV này.\n")

# Hàm cập nhật điểm số của sinh viên
def cap_nhat_diem_sinh_vien():
    mssv = input("Nhập MSSV cần cập nhật điểm: ")
    for sv in danh_sach_sinh_vien:
        if sv['MSSV'] == mssv:
            diem_moi = float(input(f"Nhập điểm mới cho sinh viên {sv['Ho Ten']}: "))
            sv['Diem'] = diem_moi
            print("Cập nhật điểm thành công!\n")
            return
    print("Không tìm thấy sinh viên có MSSV này.\n")

# Hàm xóa sinh viên theo MSSV
def xoa_sinh_vien():
    mssv = input("Nhập MSSV cần xóa: ")
    for sv in danh_sach_sinh_vien:
        if sv['MSSV'] == mssv:
            danh_sach_sinh_vien.remove(sv)
            print("Xóa sinh viên thành công!\n")
            return
    print("Không tìm thấy sinh viên có MSSV này.\n")

# Hàm hiển thị menu
def menu():
    print("Chương trình quản lý sinh viên:")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách sinh viên")
    print("3. Hiển thị danh sách sinh viên có điểm số > 7")
    print("4. Tìm kiếm sinh viên theo MSSV")
    print("5. Cập nhật điểm số của sinh viên")
    print("6. Xóa sinh viên theo MSSV")
    print("0. Thoát")

# Vòng lặp chính
while True:
    menu()
    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == '1':
        them_sinh_vien()
    elif lua_chon == '2':
        hien_thi_danh_sach_sinh_vien()
    elif lua_chon == '3':
        hien_thi_sinh_vien_diem_cao()
    elif lua_chon == '4':
        tim_kiem_sinh_vien()
    elif lua_chon == '5':
        cap_nhat_diem_sinh_vien()
    elif lua_chon == '6':
        xoa_sinh_vien()
    elif lua_chon == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.\n")
