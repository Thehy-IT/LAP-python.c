'''Bạn được cung cấp một file chứa danh sách các bài hát đã nghe của một người
dùng trên một website nghe nhạc. Trong danh sách có thể sẽ tồn tại các bài hát trùng lặp
nhau. Yêu cầu đặt ra là tạo ra file mới chứa danh sách các bài hát mà không có bài hát nào
trùng.'''
    # Hàm xử lý loại bỏ các bài hát trùng lặp và ghi ra file mới
def loai_bo_trung_lap(danh_sach_bai_hat,list_nhac_ra ):
    try:
        # Đọc nội dung từ file đầu vào
        with open(danh_sach_bai_hat, 'r', encoding='utf-8') as f:
            danh_sach_bai_hat = f.readlines()

        # Loại bỏ các bài hát trùng lặp bằng cách dùng set
        danh_sach_bai_hat_khong_trung = set(bai_hat.strip() for bai_hat in danh_sach_bai_hat)

        # Ghi các bài hát không trùng lặp vào file đầu ra
        with open(list_nhac_ra, 'w', encoding='utf-8') as f:
            for bai_hat in danh_sach_bai_hat_khong_trung:
                f.write(bai_hat + '\n')

        print("Đã tạo file mới chứa danh sách bài hát không trùng lặp.")
    
    except FileNotFoundError:
        print("Không tìm thấy file đầu vào. Vui lòng kiểm tra lại tên file.")

# Gọi hàm với tên file đầu vào và file đầu ra
danh_sach_bai_hat = 'danhsach_baihat.txt'  # Tên file chứa danh sách bài hát đã nghe
list_nhac_ra = 'danhsach_baihat_khong_trung.txt'  # Tên file mới chứa danh sách không trùng lặp
loai_bo_trung_lap(danh_sach_bai_hat, list_nhac_ra)
