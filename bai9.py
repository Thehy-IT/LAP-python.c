'''Viết chương trình yêu cầu người dùng nhập vào một chuỗi bất kỳ. Hãy định dạng
chuỗi đó sao cho không dư thừa khoảng trống ở đầu, cuối và giữa các từ chỉ chứa duy nhất
1 khoảng trống. Mỗi từ sẽ bắt đầu bằng ký tự in hoa, các ký tự còn lại là chữ in thường.'''
    # Yêu cầu người dùng nhập vào một chuỗi bất kỳ
chuoi = input("Nhập vào một chuỗi: ")

# Loại bỏ khoảng trống ở đầu và cuối, sau đó chia chuỗi thành các từ
chuoi_dinh_dang = ' '.join(chuoi.split())

# Chuyển mỗi từ sao cho ký tự đầu là chữ hoa, các ký tự còn lại là chữ thường
chuoi_dinh_dang = chuoi_dinh_dang.title()

# In ra chuỗi đã được định dạng
print("Chuỗi đã định dạng:", chuoi_dinh_dang)
