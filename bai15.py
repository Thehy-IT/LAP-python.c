'''Viết chương trình cho phép người dùng nhập vào một mảng hai chiều với mỗi phần
tử là một số nguyên, sau đó thực hiện các yêu cầu sau:
- Tính tổng các số nguyên tố trong mảng 2 chiều.
- Tính tổng đường chéo chính(trường hợp nhập vào mảng vuông)
- Tìm vị trí của phần tử nhỏ nhất và lớn nhất trong mảng 2 chiều.'''
def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố không."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nhap_mang_hai_chieu():
    """Nhập mảng hai chiều từ người dùng."""
    m = int(input("Nhập số hàng của mảng: "))
    n = int(input("Nhập số cột của mảng: "))
    mang = []
    for i in range(m):
        hang = list(map(int, input(f"Nhập các số nguyên cho hàng {i+1} (cách nhau bởi dấu cách): ").split()))
        while len(hang) != n:
            print(f"Số lượng phần tử phải là {n}. Vui lòng nhập lại:")
            hang = list(map(int, input(f"Nhập các số nguyên cho hàng {i+1} (cách nhau bởi dấu cách): ").split()))
        mang.append(hang)
    return mang

def tong_so_nguyen_to(mang):
    """Tính tổng các số nguyên tố trong mảng."""
    tong = 0
    for hang in mang:
        for num in hang:
            if is_prime(num):
                tong += num
    return tong

def tong_duong_cheo_chinh(mang):
    """Tính tổng đường chéo chính nếu mảng là vuông."""
    if len(mang) != len(mang[0]):
        return None  # Trả về None nếu không phải mảng vuông
    tong = 0
    for i in range(len(mang)):
        tong += mang[i][i]  # Thêm phần tử trên đường chéo chính
    return tong

def tim_vi_tri_min_max(mang):
    """Tìm vị trí của phần tử nhỏ nhất và lớn nhất trong mảng."""
    min_value = float('inf')
    max_value = float('-inf')
    min_pos = (-1, -1)
    max_pos = (-1, -1)

    for i in range(len(mang)):
        for j in range(len(mang[i])):
            if mang[i][j] < min_value:
                min_value = mang[i][j]
                min_pos = (i, j)
            if mang[i][j] > max_value:
                max_value = mang[i][j]
                max_pos = (i, j)

    return min_pos, max_pos

# Chương trình chính
mang_hai_chieu = nhap_mang_hai_chieu()

# Tính tổng các số nguyên tố
tong_primes = tong_so_nguyen_to(mang_hai_chieu)
print(f"Tổng các số nguyên tố trong mảng: {tong_primes}")

# Tính tổng đường chéo chính
tong_diagonal = tong_duong_cheo_chinh(mang_hai_chieu)
if tong_diagonal is not None:
    print(f"Tổng đường chéo chính: {tong_diagonal}")
else:
    print("Mảng không phải là mảng vuông, không thể tính tổng đường chéo chính.")

# Tìm vị trí của phần tử nhỏ nhất và lớn nhất
vi_tri_min, vi_tri_max = tim_vi_tri_min_max(mang_hai_chieu)
print(f"Vị trí phần tử nhỏ nhất: {vi_tri_min}")
print(f"Vị trí phần tử lớn nhất: {vi_tri_max}")
