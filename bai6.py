'''Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân
tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết
cho 5 thành dãy phân tách bởi dấu phẩy.
Ví dụ input là: 0101,1010,0111,1100 thì output sẽ là: 0101,1010'''
def kiem_tra_nhiphan(nhiphan):
    # Kiểm tra nếu độ dài khác 4 hoặc chứa ký tự không phải 0,1
    if len(nhiphan) != 4 or not all(c in '01' for c in nhiphan):
        return False
    return True

# Yêu cầu người dùng nhập vào chuỗi số nhị phân cách nhau bởi dấu phẩy
while True:
    chuoi_nhiphan = input("Nhập các số nhị phân 4 ký tự, cách nhau bởi dấu phẩy: ").split(',')
    # Kiểm tra từng chuỗi nhập vào
    if all(kiem_tra_nhiphan(nhiphan) for nhiphan in chuoi_nhiphan):
        break
    else:
        print("Vui lòng nhập lại, chỉ các số nhị phân 4 chữ số (chỉ chứa 0 và 1).")

# Tạo mảng để lưu trữ các số nhị phân chia hết cho 5
mang_nhiphan = []
for nhiphan in chuoi_nhiphan:
    thapphan = int(nhiphan, 2)  # Chuyển số nhị phân sang thập phân
    if thapphan % 5 == 0:
        mang_nhiphan.append(nhiphan)

# In ra các số nhị phân chia hết cho 5
print(','.join(mang_nhiphan))