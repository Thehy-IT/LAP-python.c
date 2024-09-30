'''Viết chương trình đọc từ file nhật ký giao dịch Transaction.txt của một tài khoản
ngân hàng. Từ đó tính ra số tiền thực tế của khách hàng đó và ghi vào một file
BalanceInquiry.txt khác với thông tin bao gồm tên và số dư hiện tại của khách hàng. Trong
đó mỗi lần rút tiền khách hàng sẽ bị tính phí 0.1% còn nộp tiền thì miễn phí.
Định dạng file nhật ký giao dịch Transaction.txt được hiển thị như sau:
Name: Vin
D 1000
W 2000

...
( Với D là nộp tiền, W là rút tiền).
Ví dụ: File nhật ký giao dịch là:

D 3000
D 2000
W 3000
D 500

Thì file BalanceInquiry.txt sẽ là: 2500'''
def tinh_so_du(file_nhat_ky, file_so_du):
    try:
        # Đọc file nhật ký giao dịch
        with open(file_nhat_ky, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Lấy tên khách hàng từ file nhật ký (nằm ở dòng đầu tiên)
        ten_khach_hang = lines[0].strip().split(": ")[1]

        # Khởi tạo số dư ban đầu là 0
        so_du = 0

        # Xử lý từng giao dịch
        for line in lines[1:]:
            giao_dich = line.strip().split()

            if giao_dich[0] == 'D':  # Giao dịch nộp tiền
                so_du += int(giao_dich[1])
            elif giao_dich[0] == 'W':  # Giao dịch rút tiền
                so_du -= int(giao_dich[1]) * 1.001  # Trừ tiền và phí 0.1%

        # Ghi kết quả vào file số dư
        with open(file_so_du, 'w', encoding='utf-8') as f:
            f.write(f"Name: {ten_khach_hang}\n")
            f.write(f"Balance: {so_du:.2f}\n")

        print("Đã tính toán và ghi số dư vào file BalanceInquiry.txt.")
    
    except FileNotFoundError:
        print("Không tìm thấy file nhật ký giao dịch. Vui lòng kiểm tra lại tên file.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Tên file đầu vào (nhật ký giao dịch) và đầu ra (số dư)
file_nhat_ky = 'Transaction.txt'
file_so_du = 'BalanceInquiry.txt'

# Gọi hàm để tính toán số dư
tinh_so_du(file_nhat_ky, file_so_du)
