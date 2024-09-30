'''Tạo từ điển Anh-Việt đơn giản bằng cách sử dụng dictionary trong Python. Chương
trình cho phép người dùng thực hiện các tính năng sau:
- Thêm các cặp từ (từ Anh và nghĩa tiếng Việt tương ứng) vào từ điển.
- Tra cứu nghĩa của từ bằng cách nhập từ tiếng Anh
- Xóa một cặp từ nào đó trong từ điển.'''
# Khởi tạo từ điển Anh-Việt
tu_dien_anh_viet = {}

# Hàm thêm cặp từ Anh-Việt vào từ điển
def them_tu():
    tu_anh = input("Nhập từ tiếng Anh: ").strip()
    nghia_viet = input("Nhập nghĩa tiếng Việt: ").strip()
    tu_dien_anh_viet[tu_anh] = nghia_viet
    print(f"Đã thêm cặp từ: {tu_anh} -> {nghia_viet}\n")

# Hàm tra cứu nghĩa của từ tiếng Anh
def tra_cuu_tu():
    tu_anh = input("Nhập từ tiếng Anh cần tra: ").strip()
    if tu_anh in tu_dien_anh_viet:
        print(f"Nghĩa của '{tu_anh}': {tu_dien_anh_viet[tu_anh]}\n")
    else:
        print(f"Từ '{tu_anh}' không có trong từ điển.\n")

# Hàm xóa một cặp từ Anh-Việt khỏi từ điển
def xoa_tu():
    tu_anh = input("Nhập từ tiếng Anh cần xóa: ").strip()
    if tu_anh in tu_dien_anh_viet:
        del tu_dien_anh_viet[tu_anh]
        print(f"Đã xóa từ '{tu_anh}' khỏi từ điển.\n")
    else:
        print(f"Từ '{tu_anh}' không có trong từ điển.\n")

# Hàm hiển thị menu
def menu():
    print("Chương trình từ điển Anh-Việt:")
    print("1. Thêm từ vào từ điển")
    print("2. Tra cứu nghĩa của từ")
    print("3. Xóa một cặp từ trong từ điển")
    print("0. Thoát")

# Vòng lặp chính
while True:
    menu()
    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == '1':
        them_tu()
    elif lua_chon == '2':
        tra_cuu_tu()
    elif lua_chon == '3':
        xoa_tu()
    elif lua_chon == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.\n")
